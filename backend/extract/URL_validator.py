from urllib.parse import urlparse


def id_extractor(url):
    """
    Extracts the tweet id from the url
    """
    id = url.split('/')[-1]

    if '?' in id:
        id = id.split('?')[0]
    elif '&' in id:
        id = id.split('&')[0]
    elif '#' in id:
        id = id.split('#')[0]
    elif not id.isdigit():
        id = None

    return id


def url_validator(url):
    """
    Validates the url
    """
    try:
        result = urlparse(url)
        # check if the url is valid and has a scheme, netloc and path
        is_valid = all([result.scheme, result.netloc, result.path])
        is_twitter_url = result.netloc.lower() in (
            'twitter.com', 'www.twitter.com')  # check if the url is from twitter
        return is_valid and is_twitter_url
    except Exception:
        return False


if __name__ == '__main__':
    url = 'https://twitter.com/realDonaldTrump/status/1346234777005284352'
    url1 = 'https://twitter.com/realDonaldTrump/status/1346234777005284352?s=20'
    url2 = 'https://twitter.com/realDonaldTrump/status/1346234777005284352&ref_url=https://www.google.com'
    url3 = 'https://google.com'
    print(id_extractor(url))
    print(id_extractor(url1))
    print(id_extractor(url2))  # works fine :)
    print(url_validator(url))
    print(url_validator(url3))
