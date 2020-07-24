from selenium import webdriver

DRIVER_PATH = './chromedriver_win32/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# Go to Reuters AAPL newsfeed
driver.get("https://www.reuters.com/companies/AAPL.OQ/news")

# Get all text within the article listing
article_listing = driver.find_element_by_xpath("//*[@id='__next']/div/div[4]/div[1]/div/div/div/div[2]/div[1]/div")

# Split text into headline and first sentence
article_listing_components = article_listing.text.split("\n")
headline = article_listing_components[0]
sentence = article_listing_components[1]

# Obtain the article for the current listing
article = driver.find_element_by_link_text(headline)
article_link = article.get_attribute("href")

# Go to current news article
driver.get(article_link)

# Retrieve date from the article
date = driver.find_element_by_class_name("ArticleHeader_date").text[0:13]

# Headline, first sentence, date
print(headline)
print(sentence)
print(date)