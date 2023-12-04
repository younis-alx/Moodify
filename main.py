from ETL.extract.twitter import Twitter
from ETL.extract.URL_validator import url_validator, id_extractor
from ETL.extract.APIKeyManager import APIKeyManager
from ETL.transform import Parser

from sentiment_analysis.v1.roberta import SentimentAnalyzer

import jmespath


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
limit = 1
continue_token = ''
url = 'https://twitter.com/freemonotheist/status/1731003302693728422'
if url_validator(url):
    id = id_extractor(url)
else:
    raise Exception('Invalid URL')

twitter = Twitter()
tweet = twitter.get_tweet(id)
tweet_parser = Parser(tweet)
#TODO: fix the pattern


# This pattern lacks the ability to check if the tweet is already in the json file
# and if it has been ran through the ML model
# and no way to check the length of the replies
# no way to store the result in the json file 
if tweet is not None:
    parsed_tweet = tweet_parser.parse_get_tweet()
    

replies = twitter.get_tweet_replies(id)

if replies['continue_token'] is not None or replies['continue_token'] != '':
    continue_token = replies['continue_token']
    while continue_token and limit > 0:
        replies = twitter.get_tweet_replies_continuation(id, continue_token)
        continue_token = replies['continue_token']
        limit -= 1

if __name__ == "__main__":
    pass













   
