import requests
from bs4 import BeautifulSoup
import json
import re
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


def getpb(url):
    browser_options = ChromeOptions()
    browser_options.headless = True
    driver = Chrome(options=browser_options)
    driver.implicitly_wait(3.5)
    driver.get(url)
    print(driver.title)
    prices = getPrices(driver)
    print("Sale Price:", prices["sale"])
    print("Old Price:", prices["old"])
    print("Original Price:", prices["original"])
    print("Normal Price:", prices["normal"])
    sizes = getSizes(driver)
    print(sizes["XXS"], sizes["XS"], sizes["S"], sizes["M"], sizes["L"], sizes["XL"])
    driver.quit()


def getPrices(driver):
    parentPriceElement = driver.find_element(By.CLASS_NAME, "prices")

    prices = {"sale": 0, "old": 0, "original": 0, "normal": 0}

    for element in parentPriceElement.find_elements(By.XPATH, "div"):
        class_name = element.get_attribute("class")
        if class_name == "sale":
            prices["sale"] = element.text
        elif class_name == "price price-old":
            prices["old"] = element.text
        elif class_name == "price price-original":
            prices["original"] = element.text
        elif class_name == "price":
            prices["normal"] = element.text

    return prices


def getSizes(driver):
    sizes = {"XXS": False, "XS": False, "S": False, "M": False, "L": False, "XL": False}

    sizeListElement = driver.find_element(By.CLASS_NAME, "c-product-info--size")
    sizeListWithLengthShadow = sizeListElement.find_element(By.XPATH, "size-selector-with-length").shadow_root
    sizeListSelectorShadow = sizeListWithLengthShadow.find_element(By.CSS_SELECTOR, "size-selector-select").shadow_root
    sizeList = sizeListSelectorShadow.find_element(By.CSS_SELECTOR, "size-list").shadow_root
    sizeListChilds = sizeList.find_elements(By.CSS_SELECTOR, "li")

    for size in sizeListChilds:
        sizeButton = size.find_element(By.CSS_SELECTOR, "button")
        sizeTextElement = sizeButton.find_element(By.CSS_SELECTOR, "span")
        sizeText = sizeTextElement.text
        sizeButtonClass = sizeButton.get_attribute("class")
        sizes[sizeText] = defineSizeBools(sizeButtonClass)

    return sizes


def defineSizeBools(sizeClass):
    return "disabled" not in sizeClass
