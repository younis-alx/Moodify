from extract.twitter import Twitter
from extract.URL_validator import url_validator, id_extractor
from extract.API_key_manager import APIKeyManager
from transform.parser import Parser
from load.storage import Storage
from sentiment_analysis.v1.roberta import SentimentAnalyzer
import concurrent.futures
import time
import tracemalloc
tracemalloc.start()
# import jmespath


"""
Puedo code:
        1. needs for parsing URL and extracting the tweet id
            - using tweet id check if the tweet is already in the json file.
                if yes, check if it been ran through the ML model if yes, check the length of the replies if the same return it.
                if no, extract the new replies and run it through the ML model and append to file return the result.
        2. make a request to the twitter API and get tweet data plus replies [shoud return 11 replies] and use (if found)
            continue_token to get the next 11 replies
        3. create a schema for the data to be stored in the json file storage using jmespath
        4. parse the data and save it in the json file

"""
def analyze_sentiment_multi_t(reply, roberta):
    result = roberta.analyze_sentiment_multi(reply['reply_text'])
    return result
def main():
    # limit = 1
    # continuation_token = ''
    url = 'https://twitter.com/freemonotheist/status/1731003302693728422'
    if url_validator(url):
        id = id_extractor(url)
    else:
        raise Exception('Invalid URL')

    twitter = Twitter()
    storge = Storage('storage.json')
    tweet = twitter.get_tweet(id) 
    tweet_parser = Parser(tweet)
    #TODO: fix the pattern

    if storge.is_tweet_in_storage(id):
        print('Tweet is already in the storage')
        if storge.load_tweet(id)['replies_count'] == len(storge.load_tweet(id)['combined_replies']):
            print('No new replies found')
            return
        else:
            print('New replies found')

    # This pattern lacks the ability to check if the tweet is already in the json file
    # and if it has been ran through the ML model
    # and no way to check the length of the replies
    if tweet is not None:
        parsed_tweet = tweet_parser.parse_get_tweet()
        replies = twitter.get_tweet_replies(id)
        if replies is not None:
            replies_parser = Parser(replies)
            parsed_replies = replies_parser.parse_get_tweet_replies()
            merged_tweet_replies = tweet_parser.merge_tweet_replies(parsed_tweet, parsed_replies)
            if storge.is_storage_empty():
                storge.save_and_overwrite(merged_tweet_replies)
            elif merged_tweet_replies['replies_count'] == len(storge.load_tweet(id)['combined_replies']) and storge.is_tweet_in_storage(id):
                print('No new replies found and tweet is already in the storage')
                return

            else:
                storge.append(merged_tweet_replies, id)
        else:
            print('No replies found')
    else:
        print('No tweet found')


    # if replies['continuation_token'] is not None or replies['continuation_token'] != '': # 
    #     continuation_token = replies['continuation_token']
    #     while continuation_token and limit > 0:
    #         break
    #     replie = twitter.get_tweet_replies_continuation(id, continuation_token)
    #     replies_parser = Parser(replie) # could be optimized using the same instance from above
    #     parsed_replies_continuation = replies_parser.parse_get_tweet_replies()
    #     print(parsed_replies_continuation)
    #     load_storage = storge.load_tweet(id)
    #     merged_tweet_replies_continuation = tweet_parser.merge_tweet_replies_continuation(load_storage, parsed_replies_continuation)
    #     storge.update(merged_tweet_replies_continuation, id)
    #     continuation_token = replie['continuation_token']
    #     limit -= 1

    tweet_storge = storge.load_tweet(id)
    roberta = SentimentAnalyzer()

    result = roberta.analyze_sentiment_multi(tweet_storge['tweet_text'])
    tweet_storge['sentiment'] = result



    start_time1 = time.perf_counter()
    for reply in tweet_storge['combined_replies']:
        result = roberta.analyze_sentiment_multi(reply['reply_text'])
        reply['sentiment'] = result
    end_time1 = time.perf_counter()
    print(f"Time taken threading: {end_time1 - start_time1:0.4f} seconds")


    
    # with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
    #         futures = {executor.submit(analyze_sentiment_multi_t, reply, roberta): reply for reply in tweet_storge['combined_replies']}
    #         for future in concurrent.futures.as_completed(futures):
    #             reply = futures[future]
    #             try:
    #                 result = future.result()
    #             except Exception as exc:
    #                 print(f'Generated an exception: {exc}')
    #             else:
    #                 reply['sentiment'] = result


    storge.update(tweet_storge, id)

if __name__ == "__main__":
    time_start = time.perf_counter()
    main()
    time_end = time.perf_counter()
    print(f"Time taken: {time_end - time_start:0.4f} seconds")













   
