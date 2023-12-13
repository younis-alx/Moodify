"""
Sentiment analysis using TextBlob library
(https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis)

"""
from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    """A mood with an emoji and a sentiment value"""
    emoji: str
    sentiment: float


def get_mood(input_text, *, threshold):
    """Return a mood based on the input text and a threshold value"""
    sentiment = TextBlob(input_text).sentiment.polarity

    friendly_threshold = threshold
    hostile_threshold = -threshold

    if sentiment >= friendly_threshold:
        return Mood(emoji="😀", sentiment=sentiment)
    elif sentiment <= hostile_threshold:
        return Mood(emoji="😡", sentiment=sentiment)
    else:
        return Mood(emoji="😐", sentiment=sentiment)
    
if __name__ == '__main__':
    while True:
        text = input("Enter some text: ")
        mood = get_mood(text, threshold=0.3)
        print(f"Mood: {mood.emoji} ({mood.sentiment})")
