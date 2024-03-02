import requests
from bs4 import BeautifulSoup
import json
import re

import html
import json
import re

def gethm_images_do_not_work_for_now(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"
    }

    session = requests.Session()
    req = session.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    results = soup.findAll("script")

    # Define the regular expression pattern to extract the dataLayerV2Json line
    pattern = re.compile(r'var productArticleDetails = (\{.*?\});', re.DOTALL)

    # Find the match for each script tag
    for script in results:
        script_text = script.string  # Extract the text content of the script tag
        if script_text:
            # Find the match
            match = pattern.search(script_text)
            # Extract and parse the JSON data
            if match:
                data = match.group(1)
                decoded_text = data.encode().decode('unicode-escape').replace("'",'"')
                decoded_text2 = json.loads(decoded_text)
                #print(data)
                print(decoded_text2)
                #print(data)




def gethm(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"
    }
    

    session = requests.Session()
    req = session.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    # Find all script tags
    script_tags = soup.find_all('script')

    #print(script_tags)
    # Loop through each script tag
    for script in script_tags:
        # Check if the script contains utag_data
        if 'utag_data = ' in script.text:
            # Extract the utag_data JSON
            utag_data_str = script.text.split('utag_data = ')[1].split(';')[0]
            original_price_start = utag_data_str.find("product_original_price")
            original_price_end = utag_data_str.find("]", original_price_start)
            original_price = utag_data_str[original_price_start:original_price_end]

            list_price_start = utag_data_str.find("product_list_price")
            list_price_end = utag_data_str.find("]", list_price_start)
            list_price = utag_data_str[list_price_start:list_price_end]

            # Printing the extracted values
            print("Product Original Price:", original_price.replace("[",'').replace('"',''))
            print("Product List Price:", list_price.replace("[",'').replace('"',''))


