import asyncio
import json

from scrapfly import ScrapeConfig, ScrapflyClient

SCRAPFLY = ScrapflyClient(key="scp-live-948f5245d5fb47ca98a66e5a56674516")

async def scrape_tweet(url: str) -> dict:
    """
    Scrape a single tweet page for Tweet thread e.g.:
    https://twitter.com/Scrapfly_dev/status/1667013143904567296
    Return parent tweet, reply tweets and recommended tweets
    """
    result = await SCRAPFLY.async_scrape(ScrapeConfig(
        url, 
        render_js=True,  # enable headless browser
        wait_for_selector="[data-testid='tweet']"  # wait for page to finish loading 
    ))
    # capture background requests and extract ones that request Tweet data
    _xhr_calls = result.scrape_result["browser_data"]["xhr_call"]
    tweet_call = [f for f in _xhr_calls if "TweetResultByRestId" in f["url"]]
    for xhr in tweet_call:
        if not xhr["response"]:
            continue
        data = json.loads(xhr["response"]["body"])
        return data['data']['tweetResult']['result']

if __name__ == "__main__":
    print(asyncio.run(scrape_tweet("https://twitter.com/Scrapfly_dev/status/1664267318053179398")))