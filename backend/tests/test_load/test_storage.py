from backend.load.storage import Storage
import pytest


def store(func):
    def wrapper(self, *args, **kwargs):
        self.storage.save_and_overwrite(self.tweet_storage)
        res = func(self, *args, **kwargs)
        self.storage.delete_all()
        return res
    return wrapper


class TestStorage:
    tweet_storage = {"1731003302693728422": {
        "tweet_id": "1731003302693728422",
        "video_url": 'null',
        "tweet_text": "#NoDesign\ud83d\ude44 https://t.co/FpjCE2Fgc5",
        "created_at": "Sat Dec 02 17:32:02 +0000 2023",
        "user_tweet": {
            "user_id": "4083072315",
            "user_name": "Paul Williams",
            "user_profile_image": "https://pbs.twimg.com/profile_images/1625943219660853257/OkDo8eTk_normal.jpg"
        },
        "replies_count": 11,
        "combined_replies": [
            {
                "tweet_id": "1731279474992283749",
                "created_at": "Sun Dec 03 11:49:27 +0000 2023",
                "reply_text": "@freemonotheist \u0648\u064e\u0641\u0650\u064a \u0627\u0644\u0652\u0623\u064e\u0631\u0652\u0636\u0650 \u0622\u064a\u064e\u0627\u062a\u064c \u0644\u0650\u0651\u0644\u0652\u0645\u064f\u0648\u0642\u0650\u0646\u0650\u064a\u0646\u064e \ufd3f\u0662\u0660\ufd3e\n \u0648\u064e\u0641\u0650\u064a \u0623\u064e\u0646\u0641\u064f\u0633\u0650\u0643\u064f\u0645\u0652 \u06da \u0623\u064e\u0641\u064e\u0644\u064e\u0627 \u062a\u064f\u0628\u0652\u0635\u0650\u0631\u064f\u0648\u0646\u064e \ufd3f\u0662\u0661\ufd3e\n\nAnd on the earth are signs for the certain [in faith] (51:20) And in yourselves. Then will you not see? (51:21)",
                "video_url": 'null',
                "media_url": 'null',
                "reply_to_tweet_id": "1731003302693728422",
                "user_replies": {
                    "user_id": "1021664176639492096",
                    "user_name": "Korhall",
                    "user_profile_image": "https://pbs.twimg.com/profile_images/1720353474964013056/PMAe7jkX_normal.jpg",
                    "location": "London, England"
                }
            },
            {
                "tweet_id": "1731036411204079688",
                "created_at": "Sat Dec 02 19:43:36 +0000 2023",
                "reply_text": "@freemonotheist Show me you don't understand evolution without telling me you don't understand evolution",
                "video_url": 'null',
                "media_url": 'null',
                "reply_to_tweet_id": "1731003302693728422",
                "user_replies": {
                    "user_id": "1161189168183201792",
                    "user_name": "AaIsrael",
                    "user_profile_image": "https://pbs.twimg.com/profile_images/1161189345132515329/PMZPbsUW_normal.jpg",
                    "location": ""
                }
            },
            {
                "tweet_id": "1731011278624186554",
                "created_at": "Sat Dec 02 18:03:44 +0000 2023",
                "reply_text": "@freemonotheist Humans weren't created by God or by random chance.\n\nWe evolved through natural selection -- and evolution can do incredible things.\n\nHere's Harvard's Mega Petri Dish showing bacteria evolve 1000x greater resistance to an antibiotic in just 11 days: https://t.co/a7XF4kCsYJ",
                "video_url": 'null',
                "media_url": [
                    "https://pbs.twimg.com/ext_tw_video_thumb/1731011005516300289/pu/img/RtTQOH8szv1XxjgE.jpg"
                ],
                "reply_to_tweet_id": "1731003302693728422",
                "user_replies": {
                    "user_id": "995006376962396160",
                    "user_name": "SDL",
                    "user_profile_image": "https://pbs.twimg.com/profile_images/1114213594097422337/An-MxMzN_normal.png",
                    "location": "any/all"
                }
            },
            {
                "tweet_id": "1731003686770368616",
                "created_at": "Sat Dec 02 17:33:34 +0000 2023",
                "reply_text": "@freemonotheist Atheist logic=CAOS",
                "video_url": 'null',
                "media_url": 'null',
                "reply_to_tweet_id": "1731003302693728422",
                "user_replies": {
                    "user_id": "4724419156",
                    "user_name": "EAGLE",
                    "user_profile_image": "https://pbs.twimg.com/profile_images/1623389659987320832/6kwb_1xA_normal.jpg",
                    "location": "Tropoj"
                }
            },
            {
                "tweet_id": "1731014412721434722",
                "created_at": "Sat Dec 02 18:16:11 +0000 2023",
                "reply_text": "@freemonotheist \u0641\u062a\u0628\u0627\u0631\u0643 \u0627\u0644\u0644\u0647 \u0627\u062d\u0633\u0646 \u0627\u0644\u062e\u0627\u0644\u0642\u064a\u0646",
                "video_url": 'null',
                "media_url": 'null',
                "reply_to_tweet_id": "1731003302693728422",
                "user_replies": {
                    "user_id": "1212820758",
                    "user_name": "Umar Matovu",
                    "user_profile_image": "https://pbs.twimg.com/profile_images/1243975339166089217/-mB1j0jd_normal.jpg",
                    "location": "Johannesburg, South Africa"
                }
            },
            {
                "tweet_id": "1730060067637166243",
                "created_at": "Thu Nov 30 03:03:57 +0000 2023",
                "reply_text": "Ashly Brianne",
                "video_url": 'null',
                "media_url": 'null',
                "reply_to_tweet_id": "1730060067637166243",
                "user_replies": {
                    "user_id": "1716075461640384512",
                    "user_name": "Ashly Brianne",
                    "user_profile_image": "https://pbs.twimg.com/profile_images/1727962768006156288/NfrPsX6v_normal.jpg",
                    "location": ""
                }
            },
            {
                "tweet_id": "1731005117141536817",
                "created_at": "Sat Dec 02 17:39:15 +0000 2023",
                "reply_text": "@freemonotheist Subhan Allah\nno doubt Allah is best creator \ud83e\udec0",
                "video_url": 'null',
                "media_url": 'null',
                "reply_to_tweet_id": "1731003302693728422",
                "user_replies": {
                    "user_id": "1386604518046113792",
                    "user_name": "Irum Chauhdry",
                    "user_profile_image": "https://pbs.twimg.com/profile_images/1709918984487768065/RROvmczk_normal.jpg",
                    "location": "Pakistan"
                }
            },
            {
                "tweet_id": "1731041985144742269",
                "created_at": "Sat Dec 02 20:05:45 +0000 2023",
                "reply_text": "@freemonotheist Someone needs to educate this guy about evolution.",
                "video_url": 'null',
                "media_url": 'null',
                "reply_to_tweet_id": "1731003302693728422",
                "user_replies": {
                    "user_id": "823701043",
                    "user_name": "Ewan Middlebin",
                    "user_profile_image": "https://pbs.twimg.com/profile_images/1724816205016358912/SIE_qtWC_normal.jpg",
                    "location": "Player#getLocation()"
                }
            },
            {
                "tweet_id": "1731007335223456070",
                "created_at": "Sat Dec 02 17:48:03 +0000 2023",
                "reply_text": "@freemonotheist LOL",
                "video_url": 'null',
                "media_url": 'null',
                "reply_to_tweet_id": "1731003302693728422",
                "user_replies": {
                    "user_id": "1161625958341890048",
                    "user_name": "JoKeR \ud83e\udd21",
                    "user_profile_image": "https://pbs.twimg.com/profile_images/1722189264824221696/Tn_2WhPZ_normal.jpg",
                    "location": "UNITED ARAB EMIRATES"
                }
            },
            {
                "tweet_id": "1731052349303501196",
                "created_at": "Sat Dec 02 20:46:56 +0000 2023",
                "reply_text": "@freemonotheist Ma ShALLAH",
                "video_url": 'null',
                "media_url": 'null',
                "reply_to_tweet_id": "1731003302693728422",
                "user_replies": {
                    "user_id": "1347493410781982725",
                    "user_name": "Shelly",
                    "user_profile_image": "https://pbs.twimg.com/profile_images/1691496072424865793/FCuahxAF_normal.jpg",
                    "location": "Pakistan"
                }
            },
            {
                "tweet_id": "1731052370019111272",
                "created_at": "Sat Dec 02 20:47:01 +0000 2023",
                "reply_text": "@freemonotheist SubhanAllah",
                "video_url": 'null',
                "media_url": 'null',
                "reply_to_tweet_id": "1731003302693728422",
                "user_replies": {
                    "user_id": "1347493410781982725",
                    "user_name": "Shelly",
                    "user_profile_image": "https://pbs.twimg.com/profile_images/1691496072424865793/FCuahxAF_normal.jpg",
                    "location": "Pakistan"
                }
            }
        ]
    }
    }

    @pytest.fixture(autouse=True)
    def setup(self):
        self.storage = Storage(
            storage_path='backend/tests/test_load/test_storage.json')

    @store
    def test_load_tweets(self):
        assert self.storage.load_tweet("53452532452345") == None
        assert self.storage.load_tweet("1731003302693728422")
        assert isinstance(self.storage.load_tweet("1731003302693728422"), dict)

    @store
    def test_load_all(self):
        assert len(self.storage.load_all()) != 0
        assert isinstance(self.storage.load_all(), dict)

    @store
    def test_append(self):
        self.storage.append("123", "test")

        assert self.storage.load_tweet("test") == "123"

    @store
    def test_update(self):
        self.storage.update("some data", "1731003302693728422")
        assert self.storage.load_tweet("1731003302693728422") == "some data"

    @store
    def test_delete_tweet(self):
        self.storage.delete_tweet("1731003302693728422")
        assert self.storage.load_tweet("test") == None

    @store
    def test_is_storage_empty(self):
        assert not self.storage.is_storage_empty()

    @store
    def test_is_tweet_in_storage(self):
        assert self.storage.is_tweet_in_storage("1731003302693728422")
        assert not self.storage.is_tweet_in_storage("123")
