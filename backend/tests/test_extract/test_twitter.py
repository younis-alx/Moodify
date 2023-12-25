import pytest
from unittest import mock
from backend.extract.twitter import Twitter


@pytest.fixture
def twitter():
    return Twitter()


@mock.patch('requests.get')
def test_get_tweet(mock_get, twitter):
    # Mock the API response
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "tweet_id": "1517995317697916928",
        "text": "Sometimes you know an exception can be thrown, and you just want to ignore it. Take advantage of the context manager, which allows you to allocate and release resources. Use “ignore instead”. Here's a full code example: Credits to: @raymondh https://t.co/ACw677xTtN",
        "media_url": [
            "https://pbs.twimg.com/media/FREAsbkXIAYiaVV.jpg"
        ],
        "video_url": None,
        "user": None,
        "creation_date": "Sun Dec 13 03:52:21 +0000 2009",
        "user_id": "96479162",
        "username": "omarmhaimdat",
        "name": "Omar MHAIMDAT",
        "follower_count": 957,
        "following_count": 1301,
        "favourites_count": 6724,
        "is_private": None,
        "is_verified": None,
        "is_blue_verified": None,
        "location": "Casablanca, Morocco",
        "profile_pic_url": "https://pbs.twimg.com/profile_images/1271521722945110016/AvKfKpLo_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/96479162/1599303392",
        "description": "Data Scientist | Software Engineer | Better programming and Heartbeat contributor",
        "external_url": "https://www.linkedin.com/in/omarmhaimdat/",
        "number_of_tweets": 3170,
        "bot": None,
        "timestamp": 1260676341,
        "has_nft_avatar": None,
        "category": None,
        "default_profile": None,
        "default_profile_image": None,
        "listed_count": 11,
        "verified_type": None,
        "language": "en",
        "favorite_count": 13,
        "retweet_count": 1,
        "reply_count": 2,
        "quote_count": 0,
        "retweet": None,
        "views": 0,
        "timestamp": 1650753261,
        "video_view_count": None,
        "in_reply_to_status_id": None,
        "quoted_status_id": None,
        "binding_values": None,
        "expanded_url": "https://twitter.com/omarmhaimdat/status/1517995317697916928/photo/1",
        "retweet_tweet_id": None,
        "extended_entities": None,
        "conversation_id": "1517995317697916928",
        "retweet_status": None,
        "quoted_status": None,
        "bookmark_count": 2,
        "source": "Twitter for Mac"
    }

    mock_get.return_value = mock_response

    # Test get_tweet method
    tweet_id = '1738370347723096152'
    tweet = twitter.get_tweet(tweet_id)

    # Assertions
    assert tweet is not None
    assert isinstance(tweet, dict)
    assert 'tweet_id' in tweet

    mock_response.status_code = 404

    assert twitter.get_tweet(tweet_id) is None

    with pytest.raises(ValueError):
        twitter.get_tweet(None)
        twitter.get_tweet('3452345')


@mock.patch('requests.get')
def test_get_tweet_replies(mock_get, twitter):
    # Mock the API response
    mock_response = mock.Mock()
    mock_response.status_code = 200

    mock_response.json.return_value = [
        {
            "tweet_id": "1349129814628773888",
            "creation_date": "Tue Jan 12 23:03:08 +0000 2021",
            "text": "@elonmusk Dear Elon, I'm a game dev. and I am making a game about colonizing Mars with you and SpaceX in it. If you think it's cool, all I need is the \"Go ahead\" to use your name and Logos. I will post this every day for a year or until I get a Yes or a No! 154 / 365",
            "media_url": "",
            "video_url": "",
            "creation_date": "Fri Jan 19 11:22:24 +0000 2018",
            "user_id": "954313086785212416",
            "username": "lvladimirovBG",
            "name": "Lyubomir Vladimirov",
            "follower_count": 12689,
            "following_count": 4,
            "favourites_count": 2811,
            "is_private": "",
            "is_verified": 0,
            "is_blue_verified": 0,
            "location": "Bulgaria",
            "profile_pic_url": "https://pbs.twimg.com/profile_images/993507603333427201/ATj7pBa4_normal.jpg",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/954313086785212416/1607242546",
            "description": "Currently developing a game about colonizing Mars.",
            "external_url": "https://marsisflat.space/",
            "number_of_tweets": 1760,
            "bot": 0,
            "timestamp": 1516360944,
            "has_nft_avatar": 0,
            "category": "",
            "default_profile": 1,
            "default_profile_image": 0,
            "listed_count": 17,
            "verified_type": "",
            "language": "en",
            "favorite_count": 23752,
            "retweet_count": 650,
            "reply_count": 517,
            "quote_count": 98,
            "retweet": 0,
            "views": "",
            "timestamp": 1610492588,
            "video_view_count": "",
            "in_reply_to_status_id": "1349129669258448897",
            "quoted_status_id": "",
            "binding_values": "",
            "expanded_url": "",
            "retweet_tweet_id": "",
            "extended_entities": "",
            "conversation_id": "1349129669258448897",
            "retweet_status": "",
            "quoted_status": "",
            "bookmark_count": 110,
            "source": "",
            "community_note": "",
        },
        {
            "tweet_id": "1349265937392930816",
            "creation_date": "Wed Jan 13 08:04:02 +0000 2021",
            "text": "@lvladimirovBG You can steal our name/logos &amp; we probably won’t sue you",
            "media_url": "",
            "video_url": "",
            "creation_date": "Tue Jun 02 20:12:29 +0000 2009",
            "user_id": "44196397",
            "username": "elonmusk",
            "name": "Elon Musk",
            "follower_count": 167148009,
            "following_count": 509,
            "favourites_count": 38423,
            "is_private": "",
            "is_verified": 0,
            "is_blue_verified": 0,
            "location": "𝕏Ð",
            "profile_pic_url": "https://pbs.twimg.com/profile_images/1683325380441128960/yRsRRjGO_normal.jpg",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/44196397/1690621312",
            "description": "",
            "external_url": "",
            "number_of_tweets": 35255,
            "bot": 0,
            "timestamp": 1243973549,
            "has_nft_avatar": 0,
            "category": "",
            "default_profile": 0,
            "default_profile_image": 0,
            "listed_count": 149507,
            "verified_type": "",
            "language": "en",
            "favorite_count": 41684,
            "retweet_count": 1498,
            "reply_count": 1123,
            "quote_count": 465,
            "retweet": 0,
            "views": "",
            "timestamp": 1610525042,
            "video_view_count": "",
            "in_reply_to_status_id": "1349129814628773888",
            "quoted_status_id": "",
            "binding_values": "",
            "expanded_url": "",
            "retweet_tweet_id": "",
            "extended_entities": "",
            "conversation_id": "1349129669258448897",
            "retweet_status": "",
            "quoted_status": "",
            "bookmark_count": 174,
            "source": "",
            "community_note": "",
        },
        {
            "continuation_token": "ZAAAAPA6HBmmgICw8bfTnMMrgIDRueyox8UrgMCxzeOaibkl5oS75b3c2pcwjMC5xdSgibklhMCsscCbibklgoDStYXCkcQrhIDQlf-s7QkA8AiwvbizzsQriICx3eL99cUrJQISFQQAAA"
        }
    ]
    mock_get.return_value = mock_response

    # Test get_tweet_replies method
    tweet_id = '1738370347723096152'
    replies = twitter.get_tweet_replies(tweet_id)

    # Assertions
    assert isinstance(replies, list)
    assert all(isinstance(reply, dict) for reply in replies)


# def test_get_tweet_replies_continuation(mock_requests, twitter):
#     # Mock the API response
#     mock_response = [
#         {
#             "tweet_id": "1349129814628773888",
#             "creation_date": "Tue Jan 12 23:03:08 +0000 2021",
#             "text": "@elonmusk Dear Elon, I'm a game dev. and I am making a game about colonizing Mars with you and SpaceX in it. If you think it's cool, all I need is the \"Go ahead\" to use your name and Logos. I will post this every day for a year or until I get a Yes or a No! 154 / 365",
#             "media_url": "",
#             "video_url": "",
#             "creation_date": "Fri Jan 19 11:22:24 +0000 2018",
#             "user_id": "954313086785212416",
#             "username": "lvladimirovBG",
#             "name": "Lyubomir Vladimirov",
#             "follower_count": 12689,
#             "following_count": 4,
#             "favourites_count": 2811,
#             "is_private": "",
#             "is_verified": 0,
#             "is_blue_verified": 0,
#             "location": "Bulgaria",
#             "profile_pic_url": "https://pbs.twimg.com/profile_images/993507603333427201/ATj7pBa4_normal.jpg",
#             "profile_banner_url": "https://pbs.twimg.com/profile_banners/954313086785212416/1607242546",
#             "description": "Currently developing a game about colonizing Mars.",
#             "external_url": "https://marsisflat.space/",
#             "number_of_tweets": 1760,
#             "bot": 0,
#             "timestamp": 1516360944,
#             "has_nft_avatar": 0,
#             "category": "",
#             "default_profile": 1,
#             "default_profile_image": 0,
#             "listed_count": 17,
#             "verified_type": "",
#             "language": "en",
#             "favorite_count": 23752,
#             "retweet_count": 650,
#             "reply_count": 517,
#             "quote_count": 98,
#             "retweet": 0,
#             "views": "",
#             "timestamp": 1610492588,
#             "video_view_count": "",
#             "in_reply_to_status_id": "1349129669258448897",
#             "quoted_status_id": "",
#             "binding_values": "",
#             "expanded_url": "",
#             "retweet_tweet_id": "",
#             "extended_entities": "",
#             "conversation_id": "1349129669258448897",
#             "retweet_status": "",
#             "quoted_status": "",
#             "bookmark_count": 110,
#             "source": "",
#             "community_note": "",
#         },
#         {
#             "tweet_id": "1349265937392930816",
#             "creation_date": "Wed Jan 13 08:04:02 +0000 2021",
#             "text": "@lvladimirovBG You can steal our name/logos &amp; we probably won’t sue you",
#             "media_url": "",
#             "video_url": "",
#             "creation_date": "Tue Jun 02 20:12:29 +0000 2009",
#             "user_id": "44196397",
#             "username": "elonmusk",
#             "name": "Elon Musk",
#             "follower_count": 167148009,
#             "following_count": 509,
#             "favourites_count": 38423,
#             "is_private": "",
#             "is_verified": 0,
#             "is_blue_verified": 0,
#             "location": "𝕏Ð",
#             "profile_pic_url": "https://pbs.twimg.com/profile_images/1683325380441128960/yRsRRjGO_normal.jpg",
#             "profile_banner_url": "https://pbs.twimg.com/profile_banners/44196397/1690621312",
#             "description": "",
#             "external_url": "",
#             "number_of_tweets": 35255,
#             "bot": 0,
#             "timestamp": 1243973549,
#             "has_nft_avatar": 0,
#             "category": "",
#             "default_profile": 0,
#             "default_profile_image": 0,
#             "listed_count": 149507,
#             "verified_type": "",
#             "language": "en",
#             "favorite_count": 41684,
#             "retweet_count": 1498,
#             "reply_count": 1123,
#             "quote_count": 465,
#             "retweet": 0,
#             "views": "",
#             "timestamp": 1610525042,
#             "video_view_count": "",
#             "in_reply_to_status_id": "1349129814628773888",
#             "quoted_status_id": "",
#             "binding_values": "",
#             "expanded_url": "",
#             "retweet_tweet_id": "",
#             "extended_entities": "",
#             "conversation_id": "1349129669258448897",
#             "retweet_status": "",
#             "quoted_status": "",
#             "bookmark_count": 174,
#             "source": "",
#             "community_note": "",
#         },
#         {
#             "continuation_token": "ZAAAAPA6HBmmgICw8bfTnMMrgIDRueyox8UrgMCxzeOaibkl5oS75b3c2pcwjMC5xdSgibklhMCsscCbibklgoDStYXCkcQrhIDQlf-s7QkA8AiwvbizzsQriICx3eL99cUrJQISFQQAAA"
#         }
#     ]
#     mock_requests.get.return_value.json.return_value = mock_response

#     # Test get_tweet_replies_continuation method
#     tweet_id = '123456789'
#     continue_token = 'abc123'
#     replies = twitter.get_tweet_replies_continuation(tweet_id, continue_token)

#     # Assertions
#     assert isinstance(replies, list)
#     assert all(isinstance(reply, dict) for reply in replies)


# def test_get_user(mock_requests, twitter):
#     # Mock the API response
#     mock_response = {
#         'id': '123456789',
#         'name': 'John Doe'
#     }
#     mock_requests.get.return_value.json.return_value = mock_response

#     # Test get_user method
#     username = 'johndoe'
#     user = twitter.get_user(username)

#     # Assertions
#     assert isinstance(user, dict)
#     assert 'id' in user
#     assert 'name' in user


# def test_get_user_tweets(mock_requests, twitter):
#     # Mock the API response
#     mock_response = [
#         {
#             'id': '987654321',
#             'text': 'Tweet 1'
#         },
#         {
#             'id': '567890123',
#             'text': 'Tweet 2'
#         }
#     ]
#     mock_requests.get.return_value.json.return_value = mock_response

#     # Test get_user_tweets method
#     username = 'johndoe'
#     tweets = twitter.get_user_tweets(username)

#     # Assertions
#     assert isinstance(tweets, list)
#     assert all(isinstance(tweet, dict) for tweet in tweets)


# def test_get_user_followers(mock_requests, twitter):
#     # Mock the API response
#     mock_response = [
#         {
#             'id': '987654321',
#             'name': 'Follower 1'
#         },
#         {
#             'id': '567890123',
#             'name': 'Follower 2'
#         }
#     ]
#     mock_requests.get.return_value.json.return_value = mock_response

#     # Test get_user_followers method
#     user_id = '123456789'
#     followers = twitter.get_user_followers(user_id)

#     # Assertions
#     assert isinstance(followers, list)
#     assert all(isinstance(follower, dict) for follower in followers)


# def test_get_user_following(mock_requests, twitter):
#     # Mock the API response
#     mock_response = [
#         {
#             'id': '987654321',
#             'name': 'Following 1'
#         },
#         {
#             'id': '567890123',
#             'name': 'Following 2'
#         }
#     ]
#     mock_requests.get.return_value.json.return_value = mock_response

#     # Test get_user_following method
#     user_id = '123456789'
#     following = twitter.get_user_following(user_id)

#     # Assertions
#     assert isinstance(following, list)
#     assert all(isinstance(follow, dict) for follow in following)


@pytest.fixture(autouse=True)
def mock_requests():
    with mock.patch('requests.get') as mock_get:
        mock_response = mock.Mock()
        mock_response.json.return_value = {
            # ... your mock response data ...
        }
        mock_get.return_value = mock_response
        yield mock_get
