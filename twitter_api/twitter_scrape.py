import tweepy
import os
import dotenv

# Load Twitter API credentialsd
dotenv.load_dotenv()


def extract_tweet_and_replies(url):
    # Twitter API credentials
    consumer_key = os.getenv('API_KEY')
    consumer_secret = os.getenv('API_KEY_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    # print(consumer_key, consumer_secret, access_token, access_token_secret)

    # Authenticate with Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, access_token, access_token_secret)
  

    # Create API object
    api = tweepy.API(auth)

    # Extract tweet ID from URL
    tweet_id = url.split('/')[-1]

    try:
        # Get the original tweet
        tweet = api.get_status(tweet_id)

        # Print the original tweet
        print('Original Tweet:')
        print(tweet.full_text)
        print('-' * 50)

        # Get replies to the tweet
        replies = tweepy.Cursor(api.search, q='to:{}'.format(tweet.user.screen_name),
                                since_id=tweet_id, tweet_mode='extended').items()

        # Print the replies
        print('Replies:')
        for reply in replies:
            if hasattr(reply, 'in_reply_to_status_id_str'):
                print(reply.full_text)
                print('-' * 50)

    except Exception as e:
        print('Error: {}'.format(str(e)))


# # Example usage
# url = 'https://twitter.com/Twitter/status/123456789'
# extract_tweet_and_replies(url)

if __name__ == '__main__':
    while True:
        url = 'https://twitter.com/ProgressiveCod2/status/1727948607863804385'
        extract_tweet_and_replies(url)