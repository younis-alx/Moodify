from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
from scipy.special import softmax

class SentimentAnalyzer:
    def __init__(self):
        # self.tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        # self.model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        # self.language_identifier = pipeline("text-classification", model="papluca/xlm-roberta-base-language-detection")
        pass
    def analyze_sentiment(self, text):
        """ Returns the sentiment scores for the given text 
            can be used for added support for more languages uses the language identifier to identify the language
            Default to English if the language is not supported
        """
        language = self.language_identifier(text, max_length=280, top_k=1, truncation=True)[0]['label']
        model_name = self.get_model_name(language)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)

        encoded_text = self.tokenizer(text, return_tensors='pt')
        output = model(**encoded_text)
        scores = output.logits[0].detach().numpy()
        scores = softmax(scores)
        return {f'roBERTa-{language}_neg': scores[0], f'roBERTa-{language}_neu': scores[1], f'roBERTa-{language}_pos': scores[2]}

    
    def analyze_sentiment_multi(self, text):
        """ Returns the sentiment scores for the given text supporting multiple languages 
            Cover the following 8 languages: Arabic, English, French, German, Hindi, Italian, Spanish, Portuguese
        """
        tokenizer =  AutoTokenizer.from_pretrained("cardiffnlp/twitter-xlm-roberta-base-sentiment")
        model =  AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-xlm-roberta-base-sentiment")
        encoded_text = tokenizer(text, return_tensors='pt')
        output = model.forward(**encoded_text)
        scores = output.logits[0].detach().numpy()
        scores = softmax(scores)
        return {f'roBERTa-neg': float(scores[0]), f'roBERTa-neu': float(scores[1]), f'roBERTa-pos': float(scores[2])} 


    def get_model_name(self, language):
        """ Returns the model name for the given language """
        
        model_map = {
            "en": "cardiffnlp/twitter-roberta-base-sentiment", # English
            "ar": "cardiffnlp/twitter-arabic-roberta-base-sentiment", # Arabic
            "fr": "cardiffnlp/twitter-french-roberta-base-sentiment", # French
            "de": "cardiffnlp/twitter-german-roberta-base-sentiment", # German
        }
        return model_map.get(language, "cardiffnlp/twitter-roberta-base-sentiment")  # Default to English model


if __name__ == '__main__':
    import time
    text = ["I love you", "Je t'aime", "Te amo", "أحبك"]
    text1 = "I love you"

    x = SentimentAnalyzer()

    start_time1 = time.perf_counter()
    result1 = x.analyze_sentiment_multi(text[-1])
    end_time1 = time.perf_counter()
    print(f"Time taken non-threading: {end_time1 - start_time1:0.4f} seconds")
    # print(result)