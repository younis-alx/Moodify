"""
This module is used to make requests to the Twitter API.
It uses the APIKeyManager class to rotate through API keys.

"""
import requests
import os
import dotenv
from APIKeyManager import APIKeyManager

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
        return response.json()
        

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
        return response.json()

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
        return response.json()

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
        return response.json()

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
        return response.json()

if __name__ == '__main__':
    twitter = Twitter()
    twitter.get_tweet('123456789')
    twitter.get_tweet('123456789')