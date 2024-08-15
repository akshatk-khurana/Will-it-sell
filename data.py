"""
Fetch images of top selling products from the Etsy developer's API and store them alongside a calculated
probability of them being sold (based off reviews and other sale metrics) in data-mappings.json
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib.request import urlretrieve
import time

URL = 'https://www.redbubble.com/shop?iaCode=u-tees&sortOrder=top%20selling'

def get_and_store_urls():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.get(URL)

    time.sleep(20)

    holder = driver.find_element(
        By.XPATH, 
        "/html/body/div[1]/div/main/div[1]/div/div/div[5]"
    )

    images = holder.find_elements(
        By.TAG_NAME, 
        "img"
    )

    print(f"Number of images found: {len(images)}")
    driver.quit()

    image_urls = []
    for img in images:
        src = img.get_attribute("src")

        if src.startswith("https://ih1.redbubble.net/image"):
            image_urls.append(src)

    existing_urls = None
    with open("urls.txt", "r") as in_file:
        existing_urls = in_file.read()
    
    with open("urls.txt", "a") as out_file:
        for url in image_urls:
            if url in existing_urls:
                continue
            else:
                out_file.write(url)
            

def download_images():
    with open("urls.txt", "r") as in_file:
        existing_urls = in_file.read().strip().split(" ")
        for url in existing_urls:
            urlretrieve(url, "test.png")


get_and_store_urls()