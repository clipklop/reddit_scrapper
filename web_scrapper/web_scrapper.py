#

import os
import json

from seleniumwire import webdriver
from seleniumwire.utils import decode as decode_sw

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/tmp/chromedriver/stable/chromedriver")



def show_request_urls(driver: webdriver, target_url: str) -> list[dict]:
    driver.get(target_url)
    return [{"url": r.url} for r in driver.requests]


def main() -> None:
    # driver = webdriver.Firefox(seleniumwire_options={'disable_encoding': True})
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    target_url = "https://www.adidas.co.uk/terrex"

    urls = show_request_urls(driver=driver, target_url=target_url)

    print(urls)


if __name__ == '__main__':
    main()

# main()   
