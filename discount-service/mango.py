import requests
from bs4 import BeautifulSoup
import json
import re


def getmango(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"
    }

    session = requests.Session()
    req = session.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    results = soup.findAll("script")

    # Define the regular expression pattern to extract the dataLayerV2Json line
    pattern = re.compile(r'var dataLayerV2Json = (\{.*?\});', re.DOTALL)

    # Find the match for each script tag
    for script in results:
        script_text = script.string  # Extract the text content of the script tag
        if script_text:
            # Find the match
            match = pattern.search(script_text)
            # Extract and parse the JSON data
            if match:
                json_data = match.group(1)
                data = json.loads(json_data)
                print(data)
                if 'ecommerce' in data and 'detail' in data['ecommerce']:
                    products = data['ecommerce']['detail']['products']
                    for product in products:
                        print("Original Price:", product['originalPrice'])
                        print("Sale Price:", product['salePrice'])
                        print("Size availability :", product['sizeAvailability'])
                        print("Size No Availability :", product['sizeNoAvailability'])

