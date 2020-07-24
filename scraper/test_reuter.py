import time

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

# Retrieve data from each article listing
for article_listing in article_listings:
    # Split text into headline and first sentence
    article_listing_components = article_listing.text.split("\n")
    headline = article_listing_components[0]
    sentence = article_listing_components[1]

    # Obtain the article for the current listing
    # article = driver.find_element_by_link_text(headline)
    # article_link = article.get_attribute("href")

    # Go to current news article
    # driver.get(article_link)

    # Retrieve date from the article
    # date = driver.find_element_by_class_name("ArticleHeader_date").text[0:13]

    # Go back to the main article listing page
    # driver.back()

    # Headline, first sentence, date
    print(headline)
    print(sentence)
    # print(date)