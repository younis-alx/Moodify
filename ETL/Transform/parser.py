import json
import jmespath
from dataclasses import dataclass

@dataclass
class Parser:
    def __init__(self, data):
        self.data = data
    
    def __dict__(self):
        return self.__object__.__dict__

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
                user: {
                        user_id: user.user_id,
                        user_name: user.name,
                        user_profile_image: user.profile_pic_url
                    }
                
            }
            """
        )
    
    def parse_get_user_followers(self):
        pass

    def parse_json(self, query):
        return json.dumps(self.parse(query))

    def parse_file(self, query, file_path):
        with open(file_path, 'w') as f:
            f.write(self.parse_json(query))

    def parse_file_append(self, query, file_path):
        with open(file_path, 'a') as f:
            f.write(self.parse_json(query))

    def parse_file_overwrite(self, query, file_path):
        with open(file_path, 'w') as f:
            f.write(self.parse_json(query))

    def parse_file_append_new_line(self, query, file_path):
        with open(file_path, 'a') as f:
            f.write('\n')
            f.write(self.parse_json(query))

    def parse_file_overwrite_new_line(self, query, file_path):
        with open(file_path, 'w') as f:
            f.write('\n')
            f.write(self.parse_json(query))

    def parse_file_append_new_line_csv(self, query, file_path):
        with open(file_path, 'a') as f:
            f.write('\n')
            f.write(self.parse(query))

    def parse_file_overwrite_new_line_csv(self, query, file_path):
        with open(file_path, 'w') as f:
            f.write('\n')
            f.write(self.parse(query))

    def parse_file_append_csv(self, query, file_path):
        with open(file_path, 'a') as f:
            f.write(self.parse(query))

    def parse_file_overwrite_csv(self, query, file_path):
        with open(file_path, 'w') as f:
            f.write(self.parse(query))

    def parse_file_append_new_line_json(self, query, file_path):
        with open(file_path, 'a') as f:
            f.write('\n')
            f.write(self.parse_json(query))

    def parse_file_overwrite_new_line_json(self, query, file_path):
        with open(file_path, 'w') as f:
            f.write('\n')
            f.write(self.parse_json(query))

    def parse_file_append_json(self, query, file_path):
        with open(file_path, 'a') as f:
            f.write(self.parse_json(query))

    def parse_file_overwrite_json(self, query, file_path):
        with open(file_path, 'w') as f:
            f.write(self.parse_json(query))

if __name__ == '__main__':
    with open('tweet.json', 'r') as f:
        data = json.load(f)
    parser = Parser(data)
    res = parser.parse(
                    """
                       replies[*].\
                       {
                        tweet_id: tweet_id
                        }
                    """
                    )# TODO: fix query
    print(vars(res))


            # video_url: video_url[1].url,
            # tweet_text: text,
            # created_at: creation_date,
            # user: {
            #         user_id: user.user_id,
            #         user_name: user.name,
            #         user_profile_image: user.profile_pic_url
            #     }
            

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