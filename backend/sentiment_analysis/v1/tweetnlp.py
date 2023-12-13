import aiohttp
import os
import dotenv
import asyncio


class InferenceAPI:
    """Class for making requests to the Inference API.

    This ML model supports the following languages:
                                                    - English
                                                    - French
                                                    - Dutch
                                                    - German
                                                    - Spanish
                                                    - Italian
                                                    - Portuguese
                                                    - Hindi
    """

    def __init__(self):
        dotenv.load_dotenv()
        self.api_url = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-xlm-roberta-base-sentiment"
        self.headers = {
            "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

    async def query(self, input):  # Added self parameter
        """Queries the API with the given input.
            param: input: The input to query the API with.
            param: tweet_id: The tweet id to query the API with.
            return: The response from the API + the tweet id.
        """
        payload = {"inputs": input}
        async with aiohttp.ClientSession() as session:
            async with session.post(self.api_url, headers=self.headers, json=payload) as response:
                return await response.json()

    async def get_result(self, merged_tweet_replies):
        tweet_results = await self.query(merged_tweet_replies['tweet_text'])
        merged_tweet_replies['tweet_sentiment'] = tweet_results

        tasks = [self.query(reply['reply_text'])
                 for reply in merged_tweet_replies['combined_replies']]

        # Await the results of the tasks
        results = await asyncio.gather(*tasks)
        for i in range(len(results)):
            merged_tweet_replies['combined_replies'][i]['sentiment'] = results[i]

        return merged_tweet_replies
