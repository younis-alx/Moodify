import os
from unittest import TestCase, mock
import unittest
from backend.extract.API_key_manager import APIKeyManager


class TestAPIKeyManager(TestCase):
    def setUp(self):
        self.api_manager = APIKeyManager()

    def test_get_next_api_key(self):
        # Mock the behavior of loading the .env file
        with mock.patch('backend.extract.API_key_manager.dotenv.load_dotenv'):
            # Mock the behavior of retrieving the API keys
            with mock.patch('backend.extract.API_key_manager.os.getenv') as mock_getenv:
                mock_getenv.return_value = 'API_KEY_1,API_KEY_2,API_KEY_3'
                api_key_1 = self.api_manager.get_next_api_key()
                api_key_2 = self.api_manager.get_next_api_key()
                api_key_3 = self.api_manager.get_next_api_key()

        self.assertEqual(api_key_1, 'API_KEY_1')
        self.assertEqual(api_key_2, 'API_KEY_2')
        self.assertEqual(api_key_3, 'API_KEY_3')

    def test_reset_api_keys(self):
        # Mock the behavior of loading the .env file
        with mock.patch('backend.extract.API_key_manager.dotenv.load_dotenv'):
            # Mock the behavior of resetting the API keys
            with mock.patch('backend.extract.API_key_manager.APIKeyManager.reset_api_keys') as mock_reset:
                self.api_manager.reset_api_keys()

        mock_reset.assert_called_once()

    def test_append_api_key(self):
        # Mock the behavior of appending the API key to the .env file
        with mock.patch('backend.extract.API_key_manager.APIKeyManager.append_api_key') as mock_append:
            self.api_manager.append_api_key('.env', 'test', 'test')

        mock_append.assert_called_once_with('.env', 'test', 'test')

    def test_init_loads_env_file(self):
        # Mock the behavior of loading the .env file
        with mock.patch('backend.extract.API_key_manager.dotenv.load_dotenv') as mock_load_dotenv:
            self.api_manager.__init__()

        mock_load_dotenv.assert_called_once()

    def test_get_next_api_key_returns_none_when_no_keys(self):
        # Mock the behavior of loading the .env file
        with mock.patch('backend.extract.API_key_manager.dotenv.load_dotenv'):
            # Mock the behavior of retrieving the API keys
            with mock.patch('backend.extract.API_key_manager.os.getenv') as mock_getenv:
                mock_getenv.return_value = None
                api_key = self.api_manager.get_next_api_key()

        self.assertIsNone(api_key)

    def test_append_api_key_appends_to_env_file(self):
        # Mock the behavior of appending the API key to the .env file
        with mock.patch('backend.extract.API_key_manager.APIKeyManager.append_api_key') as mock_append:
            self.api_manager.append_api_key('.env', 'test', 'test')

        mock_append.assert_called_once_with('.env', 'test', 'test')

    def test_reset_api_keys_calls_append_api_key_with_first_key(self):
        # Mock the behavior of appending the API key to the .env file
        with mock.patch('backend.extract.API_key_manager.APIKeyManager.append_api_key') as mock_append:
            self.api_manager.reset_api_keys()

        mock_append.assert_called_once_with('.env', 'API_KEY_1', 'X_API_KEY')


if __name__ == '__main__':
    unittest.main()
