from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


def gethm(url):
    browser_options = ChromeOptions()
    browser_options.headless = True
    driver = Chrome(options=browser_options)
    driver.implicitly_wait(3.5)
    driver.get(url)
    print(driver.title)

    prices =getPrices(driver)
    getSizes(driver)
    driver.quit()


def getPrices(driver):
    parentPriceElement = driver.find_element(by=By.CLASS_NAME, value="e26896")


    #first index is sale price, second index is normal price
    prices = ["0", "0"]
    i = 0
    if '%' in parentPriceElement.text:
        #there is discount
        for price in parentPriceElement.find_elements(by=By.XPATH, value="span"):
            prices[i] = (price.text)
            i = i + 1
    else:
        #there is no discount
        prices[1] = (parentPriceElement.find_element(by=By.XPATH, value="span").text)


def getSizes(driver):
    parentSizeElement = driver.find_elements(by=By.CLASS_NAME, value="ListGrid-module--item__3n3A-")
    isAvailable = False
    for size in parentSizeElement:
        labelElement = size.find_element(by=By.XPATH, value="label")
        sizeElement = labelElement.get_attribute("for")
        if labelElement.get_attribute("aria-disabled"):
            isAvailable = False
        else:
            isAvailable = True

        print("size ", sizeElement, "is available ", isAvailable)