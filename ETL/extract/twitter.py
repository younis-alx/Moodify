"""
This module is used to make requests to the Twitter API.
It uses the APIKeyManager class to rotate through API keys.

"""
import requests
import os
import dotenv
import json
from APIKeyManager import APIKeyManager
# from Transform.parser import Parser

class Twitter:
    def __init__(self):
        dotenv.load_dotenv()
        self.api_key = APIKeyManager()
        self.api_host = os.getenv('X-API-HOST')
        

    def get_tweet(self, tweet_id):
        """Returns the tweet details with the given tweet ID"""

        if len(tweet_id) != 19:
            raise ValueError('Tweet ID must be 19 characters long')
        elif tweet_id is None:
            raise ValueError('Tweet ID cannot be None')
        
        api = self.api_key.get_next_api_key()
        url = "https://twitter154.p.rapidapi.com/tweet/details"
        querystring = {"tweet_id": tweet_id}
        headers = {
            "X-RapidAPI-Key": api,
            "X-RapidAPI-Host": self.api_host
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        return None
    

    def get_tweet_replies(self, tweet_id):
        """Returns the replies of the tweet with the given tweet ID"""
        if len(tweet_id) != 19:
            raise ValueError('Tweet ID must be 19 characters long')
        elif tweet_id is None:
            raise ValueError('Tweet ID cannot be None')
        # elif limit is None:
        #     raise ValueError('Limit cannot be None')
        # elif limit < 1 or limit > 100:
        #     raise ValueError('Limit must be between 1 and 100')
        
        api = self.api_key.get_next_api_key()
        url = "https://twitter154.p.rapidapi.com/tweet/replies"
        querystring = {
            "tweet_id": tweet_id,
            }
        headers = {
            "X-RapidAPI-Key": api,
            "X-RapidAPI-Host": self.api_host
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        return None
    

    def get_tweet_replies_continuation(self, tweet_id, continue_token, limit=2):
        """Returns the replies of the tweet with the given tweet ID"""
        if len(tweet_id) != 19:
            raise ValueError('Tweet ID must be 19 characters long')
        elif tweet_id is None:
            raise ValueError('Tweet ID cannot be None')
        elif continue_token is None:
            raise ValueError('Continue token cannot be None')
        elif limit is None:
            raise ValueError('Limit cannot be None')
        elif limit <= 1 or limit > 100:
            raise ValueError('Limit must be between 1 and 100')
        # elif len(continue_token) != 36:
        #     raise ValueError('Continue token must be 36 characters long')
        elif continue_token == '' or continue_token == ' ': 
            raise ValueError('Continue token cannot be empty')
        
        
        api = self.api_key.get_next_api_key()
        url = "https://twitter154.p.rapidapi.com/tweet/replies"
        querystring = {
            "tweet_id": tweet_id,
            "continue_token": continue_token,
            }
        headers = {
            "X-RapidAPI-Key": api,
            "X-RapidAPI-Host": self.api_host
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        return None
        


    def get_user(self, username):
        """Returns the user details with the given username"""
        if username is None:
            raise ValueError('Username cannot be None')
        elif len(username) < 4 or len(username) > 15:
            raise ValueError('Username must be between 4 and 15 characters long')
        
        api = self.api_key.get_next_api_key()
        url = "https://twitter154.p.rapidapi.com/user/details"
        querystring = {"username": username}
        headers = {
            "X-RapidAPI-Key": api,
            "X-RapidAPI-Host": self.api_host
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        return None


    def get_user_tweets(self, username, limit=10, include_replies=False, include_pinned=False):
        """Returns the tweets of the user with the given username"""
        if username is None:
            raise ValueError('Username cannot be None')
        elif len(username) < 4 or len(username) > 15:
            raise ValueError('Username must be between 4 and 15 characters long')
        elif limit is None:
            raise ValueError('Limit cannot be None')
        elif limit < 1 or limit > 100:
            raise ValueError('Limit must be between 1 and 100')
        
        api = self.api_key.get_next_api_key()
        url = "https://twitter154.p.rapidapi.com/user/tweets"
        querystring = {
            "username": username,
            "limit": str(limit),
            "include_replies": (include_replies and "true" or "false"),
            "include_pinned": (include_pinned and "true" or "false"),
            }
        headers = {
            "X-RapidAPI-Key": api,
            "X-RapidAPI-Host": self.api_host
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        return None


    def get_user_followers(self, user_id, limit=5):
        """Returns the followers of the user with the given user ID"""
        if user_id is None:
            raise ValueError('User ID cannot be None')
        elif limit is None:
            raise ValueError('Limit cannot be None')
        elif limit < 1 or limit > 100:
            raise ValueError('Limit must be between 1 and 100')
        
        api = self.api_key.get_next_api_key()
        url = "https://twitter154.p.rapidapi.com/user/followers"
        querystring = {
            "user_id": user_id,
            "limit": str(limit)
            }
        headers = {
            "X-RapidAPI-Key": api,
            "X-RapidAPI-Host": self.api_host
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        return None


    def get_user_following(self, user_id, limit=5):
        """Returns the users followed by the user with the given user ID"""
        
        if user_id is None:
            raise ValueError('User ID cannot be None')
        elif limit is None:
            raise ValueError('Limit cannot be None')
        elif limit < 1 or limit > 100:
            raise ValueError('Limit must be between 1 and 100')
        
        api = self.api_key.get_next_api_key()
        url = "https://twitter154.p.rapidapi.com/user/following"
        querystring = {
            "user_id": user_id,
            "limit": str(limit)
            }
        headers = {
            "X-RapidAPI-Key": api,
            "X-RapidAPI-Host": self.api_host
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()
        return None


if __name__ == '__main__':
    twitter = Twitter()
    res = twitter.get_tweet_replies('1729675116609429582')
    # res.parse()
    with open('replies.json', 'w+') as f:
        json.dump(res, f, indent=4)
    # twitter.get_tweet('123456789')