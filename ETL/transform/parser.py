import json
import jmespath
from dataclasses import dataclass

@dataclass
class Parser:
    def __init__(self, data):
        self.data = data

    def parse(self, query):
        return jmespath.search(query, self.data)
    
    def parse_get_tweet(self):
        return self.parse(
            """
            {
                tweet_id: tweet_id,
                video_url: video_url[1].url,
                tweet_text: text,
                created_at: creation_date,
                user_tweet: {
                        user_id: user.user_id,
                        user_name: user.name,
                        user_profile_image: user.profile_pic_url
                    }
                
            }
            """
        )
    
    def parse_get_tweet_replies(self):
        res = self.parse(
                    "replies | \
                       {\
                       replies_count: length(@),\
                       combined_replies: [*].\
                       {\
                       tweet_id: tweet_id,\
                       created_at: creation_date, \
                       reply_text: text, \
                       video_url: video_url, \
                       media_url: media_url, \
                       reply_to_tweet_id: conversation_id, \
                       user_replies: \
                       {\
                       user_id: user.user_id, \
                       user_name: user.name, \
                       user_profile_image: user.profile_pic_url, \
                       location: user.location\
                       }}}"
        )
        return res

    def merge_tweet_replies(self, tweet_data, replies_data):
        """Merge tweet data and replies data into one object"""
        tweet_data['replies_count'] = replies_data['replies_count']
        tweet_data['combined_replies'] = replies_data['combined_replies']
        return {tweet_data['tweet_id']: tweet_data}
    

if __name__ == '__main__':
    with open('tweet.json', 'r') as f:
        tweet = json.load(f)
    with open('replies.json', 'r') as f:
        replies = json.load(f)
    parser = Parser(tweet)
    res = parser.merge_tweet_replies(tweet, replies)
    with open('storage.json', 'w') as f:
        json.dump(res, f, indent=4)

    print(res) 

            

    # parser.parse_file_overwrite('text', 'text.txt')
    # parser.parse_file_append('text', 'text.txt')
    # parser.parse_file_overwrite_new_line('text', 'text.txt')
    # parser.parse_file_append_new_line('text', 'text.txt')
    # parser.parse_file_overwrite_csv('text', 'text.csv')
    # parser.parse_file_append_csv('text', 'text.csv')
    # parser.parse_file_overwrite_new_line_csv('text', 'text.csv')
    # parser.parse_file_append_new_line_csv('text', 'text.csv')
    # parser.parse_file_overwrite_json('text', 'text.json')
    # parser.parse_file_append_json('text', 'text.json')
    # parser.parse_file_overwrite_new_line_json('text', 'text.json')
    # parser.parse_file_append_new_line_json('text', 'text.json')