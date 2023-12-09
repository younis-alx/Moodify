from backend.load import storage
from backend.api.v1.views import app_views
from flask import jsonify, request, abort
from flasgger.utils import swag_from


@app_views.route('/tweets', methods=['GET'], strict_slashes=False)
@swag_from('documentation/tweets/all_tweets.yml', methods=['GET'])
def get_tweets():
    """ Retrieves the list of all Tweet objects """
    tweets = storage.load_all()
    list_tweets = []
    for tweet in tweets.values():
        list_tweets.append(tweet)
        
    return jsonify(tweets)
