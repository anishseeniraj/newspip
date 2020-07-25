import time

import pandas as pd
import numpy as np
from selenium import webdriver


def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height


DRIVER_PATH = "D:/talks-of-stocks/scraper/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# Wait before throwing an exception
driver.implicitly_wait(30)

# Go to Reuters AAPL newsfeed
driver.get("https://www.reuters.com/companies/AAPL.OQ/news")
scroll(driver, 5)

# Get all text within the article listing
# article_listing = driver.find_element_by_xpath("//*[@id='__next']/div/div[4]/div[1]/div/div/div/div[2]/div[1]/div")

# Store all the article listings
article_listings = []
article_listings = driver.find_elements_by_class_name("MarketStoryItem-container-3rpwz")

data = []

# Retrieve data from each article listing
for article_listing in article_listings:
    # Holds current article's details
    article_details = []

    # Split text into headline and first sentence
    article_listing_components = article_listing.text.split("\n")
    headline = article_listing_components[0]
    sentence = article_listing_components[1]

    # Obtain the article for the current listing
    article = driver.find_element_by_link_text(headline)
    article_link = article.get_attribute("href")

    # Go to current news article in a new window
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(article_link)

    # Retrieve date from the article
    date = driver.find_element_by_class_name("ArticleHeader_date").text[0:13]

    # Go back to the main article listings window
    driver.close()
    driver.switch_to_window(driver.window_handles[0])

    # Appending data to current article details
    article_details.append(date)
    article_details.append(headline)
    article_details.append(sentence)

    # Appending current article details to final data list
    data.append(article_details)

# Obtaining individual columns
data = np.array(data)
dates = data[:, 0]
headlines = data[:, 1]
sentences = data[:, 2]
column_headers = ["Date", "Headline", "Sentence"]

# Wrapping a pandas DataFrame around the data
aapl_news = pd.DataFrame(columns=column_headers)
aapl_news["Date"] = dates
aapl_news["Headline"] = headlines
aapl_news["Sentence"] = sentences

# Exporting news data to a CSV
aapl_news.to_csv("aapl_news.csv", index=False)