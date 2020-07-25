from selenium import webdriver
import pandas as pd
import numpy as np
from utils import scroll


class Reuters:
    url_scheme = "https://"
    url_host = "www.reuters.com/"
    url_path = "companies/"
    driver_path = "D:/talks-of-stocks/scraper/chromedriver_win32/chromedriver.exe"


    def __init__(self, ticker):
        self.ticker = ticker
        self.url = self.url_scheme + self.url_host + self.url_path + self.ticker + ".OQ/news"
        self.driver = webdriver.Chrome(executable_path=self.driver_path)

        self.driver.implicitly_wait(30)


    def open_newsfeed(self):
        self.driver.get(self.url)
        # scroll(self.driver, 5)


    def get_article_listings(self):
        self.article_listings = self.driver.find_elements_by_class_name("MarketStoryItem-container-3rpwz")


    def get_data(self):
        self.data = []

        for article_listing in self.article_listings:
            # Store current article details
            article_details = []

            # Retrieve headline and first sentence
            article_listing_components = article_listing.text.split("\n")
            headline = article_listing_components[0]
            sentence = article_listing_components[1]

            # Retrieve current article href
            article = self.driver.find_element_by_link_text(headline)
            article_link = article.get_attribute("href")

            # Open current article in a new tab
            self.driver.execute_script("window.open('');")
            self.driver.switch_to_window(self.driver.window_handles[1])
            self.driver.get(article_link)

            # Retrieve article date
            date = self.driver.find_element_by_class_name("ArticleHeader_date").text[0:13]

            # Go back to main article listings tab
            self.driver.close()
            self.driver.switch_to_window(self.driver.window_handles[0])

            # Store current article details
            article_details.append(date)
            article_details.append(headline)
            article_details.append(sentence)

            # Storing current article details in the dataset
            self.data.append(article_details)


    def export_data(self):
        # Obtaining individual columns
        data = np.array(self.data)
        dates = data[:, 0]
        headlines = data[:, 1]
        sentences = data[:, 2]
        column_headers = ["Date", "Headline", "Sentence"]

        # Pandas DataFrame wrapper
        self.dataset = pd.DataFrame(columns=column_headers)
        self.dataset["Date"] = dates
        self.dataset["Headline"] = headlines
        self.dataset["Sentence"] = sentences

        # Exporting news data to CSV
        self.dataset.to_csv(self.ticker + "_news.csv", index=False)


# aapl_scraper = Reuters("AAPL")
# aapl_scraper.open_newsfeed()
# aapl_scraper.get_article_listings()
# aapl_scraper.get_data()
# aapl_scraper.export_data()
