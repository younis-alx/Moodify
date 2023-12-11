from backend.load import storage
from backend.api.v1.views import app_views
from flask import jsonify, request, abort
from flasgger.utils import swag_from
from backend.sentiment_analysis.v1.tweetnlp import InferenceAPI
from backend.extract.URL_validator import url_validator, id_extractor
from backend.transform.parser import Parser
from backend.extract.twitter import Twitter
import nest_asyncio
import asyncio


@app_views.route('/tweets', methods=['GET'], strict_slashes=False)
@swag_from('documentation/tweets/all_tweets.yml', methods=['GET'])
def get_tweets():
    """ Retrieves the list of all Tweet objects """
    tweets = storage.load_all()
    if tweets is None:
        tweets = {'message': 'storage is empty'}

    return jsonify(tweets)


@app_views.route('/tweets/<tweet_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/tweets/get_tweet.yml', methods=['GET'])
def get_tweet(tweet_id):
    """ Retrieves a Tweet object """
    tweet = storage.load_tweet(tweet_id)
    if tweet is None:
        abort(404, description="Tweet not found")
    return jsonify(tweet)


@app_views.route('/tweets', methods=['POST'], strict_slashes=False)
@swag_from('documentation/tweets/create_tweet.yml', methods=['POST'])
def create_tweet():
    """ Creates a Tweet """
    twitter = Twitter()

    data = request.get_json()
    url = data.get('url')

    if url_validator(url) and id_extractor(url):
        id = id_extractor(url)
    else:
        abort(400, description="Invalid URL")

    if storage.is_tweet_in_storage(id):
        return jsonify(storage.load_tweet(id))

    tweet = twitter.get_tweet(id)

    if tweet is None:
        abort(404, description="Tweet not found")

    tweet_parser = Parser(tweet)
    parsed_tweet = tweet_parser.parse_get_tweet()

    tweet_replies = twitter.get_tweet_replies(id)
    replies_parser = Parser(tweet_replies)
    parsed_replies = replies_parser.parse_get_tweet_replies()
    try:
        merged_tweet_replies = tweet_parser.merge_tweet_replies(
            parsed_tweet, parsed_replies)
    except Exception as e:
        abort(500, description=str(e))

    roberta = InferenceAPI()

    tweet_results = nest_asyncio.run(
        roberta.query(merged_tweet_replies['tweet_text']))
    merged_tweet_replies['tweet_sentiment'] = tweet_results

    tasks = [roberta.query(reply['reply_text'])
             for reply in merged_tweet_replies['combined_replies']]

    # Await the results of the tasks
    results = nest_asyncio(asyncio.gather(*tasks))
    for i in range(len(results)):
        merged_tweet_replies['combined_replies'][i]['sentiment'] = results[i]

    if storage.is_storage_empty():
        storage.save_and_overwrite(merged_tweet_replies)
    else:
        storage.append(merged_tweet_replies, id)

    return jsonify(merged_tweet_replies)
