"""
Sentiment analysis using TextBlob
"""
from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input_text, *, threshold):
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
        text: str = input("Enter some text: ")
        mood: Mood = get_mood(text, threshold=0.3)
        print(f"Mood: {mood.emoji} ({mood.sentiment})")
