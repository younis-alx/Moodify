import snscrape.modules.twitter as sntwitter
import pandas as pd


query = 'python'
tweets = []
tweet_limit = 10 

try:
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        # print(tweet)
        # break
        if len(tweets) >= tweet_limit:
            break
        else:
            tweets.append([tweet.date, 
                        tweet.id, 
                        tweet.content, 
                        tweet.user.username])
except Exception as e:
    print('Error: {}'.format(str(e)))
    
df = pd.DataFrame(tweets, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

print(df.head())

# if __name__ == '__main__':
#     print(df.head())
#     print(df.shape)
#     print(df.columns)
#     print(df.info())
#     print(df.describe())
#     print(df['Text'].head())
#     print(df['Text'].tail())
#     print(df['Text'].sample(5))
#     print(df['Text'].str.contains('python').head())
#     print(df['Text'].str.contains('python').sum())
#     print(df['Text'].str.contains('python').mean())
#     print(df['Text'].str.contains('python').value_counts())
#     print(df['Text'].str.contains('python').value_counts(normalize=True))
#     print(df['Text'].str.contains('python').value_counts(normalize=True).mul(100).round(1).astype(str) + '%')
#     print(df['Text'].str.contains('python').value_counts(normalize=True).mul(100).round(1).astype(str) + '%')
#     print(df['Text'].str.contains('python').value_counts(normalize=True).mul(100).round(1).astype(str) + '%')
#     print(df['Text'].str.contains('python').value_counts(normalize=True).mul(100).round(1).astype(str) + '%')
#     print(df['Text'].str.contains('python').value_counts(normalize=True).mul(100).round(1).astype(str) + '%')
#     print(df['Text'].str.contains('python').value_counts(normalize=True).mul(100).round(1).astype(str) + '%')
#     print(df['Text'].str.contains('python').value_counts(normalize=True).mul(100).round(1).astype(str) + '%')
#     print(df['Text'].str.contains('python').value_counts(normalize=True).mul(100).round(1).astype(str) + '%')
#     print(df['Text'].str.contains('python').value_counts(normalize=True).mul(100).round(1).astype(str) + '%')

#     print(df['Text'].str.contains('python').value_counts(normalize=True).mul(100).round(1).astype(str) + '%')
#     print(df['Text'].str.contains('python').value_counts(normalize=True).mul(100).round(1).astype(str) + '%')

#     print(df['Text'].str.contains('python').value_counts(normalize=True).mul(100).round(1).astype(str) + '%')