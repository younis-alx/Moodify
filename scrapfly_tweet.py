import json
from asyncio import run
import os
import dotenv
from scrapfly import ScrapeConfig, ScrapflyClient, UpstreamHttpClientError, \
ScrapflyScrapeError, UpstreamHttpServerError

dotenv.load_dotenv()

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
    SCRAPFLY = ScrapflyClient(key=os.getenv("SCRAPFLY_KEY"))
    try:
        result = await SCRAPFLY.async_scrape(ScrapeConfig(
            url, 
            render_js=True,  # enable headless browser
            rendering_wait=1000, # wait for 1 second before scraping
            cache=True, # enable cache for 1 day default
            cache_clear=True, # clear cache before scraping
            screenshots={"page": "fullpage"}, # take a screenshot of the page
            asp=True, # enable automatic smart pagination
            debug=True, # enable debug mode
            auto_scroll=True, # enable auto scroll
            wait_for_selector="[data-testid='tweet']",  # wait for page to finish loading
        ))
    except UpstreamHttpServerError as e:  # 5xx error
        print(e.api_response.scrape_result['error'])
        raise e
    except UpstreamHttpClientError as e: # 4xx error
        print(e.api_response.scrape_result['error'])
        raise e
    # UpstreamHttpError can be used to catch all related error regarding the upstream website
    except ScrapflyScrapeError as e:
        print(e.message)
        print(e.code)
        raise e

    write_output_to_file(result.scrape_result['screenshots'], "screenshots.json")
    # capture background requests and extract ones that request Tweet data
    _xhr_calls = result.scrape_result["browser_data"]["xhr_call"]

    tweet_call = [f for f in _xhr_calls if "TweetResultByRestId" in f["url"]]

    for xhr in tweet_call:
        if not xhr["response"]:
            continue
        data = json.loads(xhr["response"]["body"])
        write_output_to_file(data['data'], "data.json")
        return data['data']['tweetResult']['result']
    
def fetch_tweet(url: str) -> dict:
    """fetch tweet data from url"""
    return run(scrape_tweet(url))







if __name__ == "__main__":
    print(run(scrape_tweet(input("Enter tweet url: "))))



