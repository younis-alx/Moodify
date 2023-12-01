""" This module is used to manage the API keys used to access the Twitter API
    The API keys are stored in a .env file in the root directory of the project
    The .env file should have the following format:
    [ENV_USAGE]:
        X-API-KEY="API_KEY_1,API_KEY_2,API_KEY_3"
"""
import os
import dotenv
import itertools


class APIKeyManager:
    def __init__(self):
        # Load the .env file
        dotenv.load_dotenv()
        self.api_keys = itertools.cycle(os.getenv('X-API-KEY').split(','))

    def get_next_api_key(self):
        """Returns the next API key in the list"""""
        return next(self.api_keys)
    @property
    def reset_api_keys(self):
        """Resets the API keys to the first one in the list"""""
        self.api_keys = itertools.cycle(os.getenv('X-API-KEY').split(','))





if __name__ == '__main__':
    # Example usage
    api_manager = APIKeyManager()
    API_KEY_1 = api_manager.get_next_api_key()
    print(API_KEY_1, len(API_KEY_1)) # API_KEY_1
    API_KEY_2 = api_manager.get_next_api_key()
    print(API_KEY_2, len(API_KEY_2)) # API_KEY_2
    API_KEY_3 = api_manager.get_next_api_key()
    print(API_KEY_3, len(API_KEY_3)) # API_KEY_3
    api_manager.reset_api_keys # REST TO API_KEY_1
    API_KEY_1 = api_manager.get_next_api_key()
    print(API_KEY_1, len(API_KEY_1)) # API_KEY_1

        
