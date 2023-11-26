import json
from asyncio import run

from scrapfly import ScrapeConfig, ScrapflyClient

SCRAPFLY = ScrapflyClient(key="scp-live-948f5245d5fb47ca98a66e5a56674516")

def write_output_to_file(output, file_path):

    # Open the file in write mode and create it if it doesn't exist
    with open(file_path, "w+") as file:
        # Write the output to the file
        file.write(str(output))


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
    # write_output_to_file(result.scrape_result, "result_scrape.json")
    # capture background requests and extract ones that request Tweet data
    _xhr_calls = result.scrape_result["browser_data"]["xhr_call"]
    # write_output_to_file(_xhr_calls, "xhr_calls.json")
    tweet_call = [f for f in _xhr_calls if "TweetResultByRestId" in f["url"]]
    # write_output_to_file(tweet_call, "tweet_call.json")
    for xhr in tweet_call:
        if not xhr["response"]:
            continue
        data = json.loads(xhr["response"]["body"])
        return data['data']['tweetResult']['result']
    
def fetch_tweet(url: str) -> dict:
    return run(scrape_tweet(url))







if __name__ == "__main__":
    print(run(scrape_tweet(input("Enter tweet url: "))))