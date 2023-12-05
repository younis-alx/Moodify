import json

"""This module is responsible for interacting with json file"""

class Storage:
    def __init__(self, storage_path):
        try:
            with open(storage_path, "r") as f:
                json.load(f)
        except FileNotFoundError:
            with open(storage_path, "w") as f:
                json.dump({}, f, indent=4)
        self.storage_path = storage_path
    

    def save_and_overwrite(self, data):
        """Save data to json file"""
        with open(self.storage_path, 'w') as f:
            json.dump(data, f, indent=4)


    def update(self, data, key):
        """Update data in json file"""
        with open(self.storage_path, 'r') as f:
            storage = json.load(f)
        if key in storage:
            storage[key] = data
            self.save_and_overwrite(storage)
        else:
            print('Key not found in storage try append instead')

    def append(self, data, key):
        """Append data to json file"""
        with open(self.storage_path, 'r') as f:
            storage = json.load(f)
        if key not in storage:
            storage[key].append(data)
            self.save_and_overwrite(storage)
        else:
            print('Existing key found in storage try update instead')


    def load_tweet(self, tweet_id):
        """Load data from json file"""
        with open(self.storage_path, 'r') as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = {}
        return data.get(tweet_id, None)
    

    def load_all(self):
        """Load all data from json file"""
        with open(self.storage_path, 'r') as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = {}
        return data

    def delete_tweet(self, key):
        """Delete data from json file"""
        with open(self.storage_path, 'r') as f:
            storage = json.load(f)
        if key in storage:
            del storage[key]
            self.save_and_overwrite(storage)
        else:
            print('Key not found in storage')

    def delete_all(self):
        """Delete all data from json file"""
        with open(self.storage_path, 'w') as f:
            json.dump({}, f, indent=4)
    
    def is_storage_empty(self):
        """Check if the json file is empty"""
        with open(self.storage_path, 'r') as f:
            storage = json.load(f)
        return len(storage) == 0


if __name__ == '__main__':
    with open('tweet.json', 'r') as f:
        tweet = json.load(f)
    with open('replies.json', 'r') as f:
        replies = json.load(f)
    storage = Storage('storage.json')

    print(storage.load_tweet('17296751166094295820'))
    print(storage.load_tweet('1729675116609429580'))
        

    
    