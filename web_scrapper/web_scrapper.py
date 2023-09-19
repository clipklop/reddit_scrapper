#

import json

from seleniumwire import webdriver
from seleniumwire.utils import decode as decode_sw


def show_request_urls(driver: webdriver, target_url: str) -> list[dict]:
    driver.get(target_url)
    return [{"url": r.url} for r in driver.requests]


def main() -> None:
    # driver = webdriver.Firefox(seleniumwire_options={'disable_encoding': True})
    driver = webdriver.Chrome()
    target_url = "https://www.adidas.co.uk/terrex"

    urls = show_request_urls(driver=driver, target_url=target_url)

    print(urls)


if __name__ == '__main__':
    main()

# main()   
