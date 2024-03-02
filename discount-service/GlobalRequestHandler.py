from urllib.request import Request, urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
def checkURL(requested_url):
    if not urlparse(requested_url).scheme:
        requested_url = "https://" + requested_url
    return requested_url


def requestAndParse(requested_url):
    requested_url = checkURL(requested_url)
    try:
        # define headers to be provided for request authentication
        request_headers = {
            'referer': 'https://scrapeme.live/shop/',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'sec-ch-device-memory': '8',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
            'sec-ch-ua-platform': "Linux",
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-ch-viewport-width': '792',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }
        request_obj = Request(url = requested_url, headers = request_headers)
        opened_url = urlopen(request_obj)
        page_html = opened_url.read()
        opened_url.close()
        page_soup = BeautifulSoup(page_html, "html.parser")
        return page_soup, requested_url

    except Exception as e:
        print(e)