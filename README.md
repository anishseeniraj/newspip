# Newspip

Supposedly, feature engineering is cool. <a href="[https://github.com/anishseeniraj/stockastic](https://github.com/anishseeniraj/stockastic)">Stockastic</a> is okay and all, but surely raw time series forecasting isn't the way to go for predicting stock prices. Incorporate this NLP pipeline in your projects if you want more accurate stock forecasts with an additional feature (company financial news).

## Table of Contents

* [Introduction](#introduction)
  * [Newspip](#newspip)
  * [Use Cases](#use-cases)
* [Built With](#built-with)
* [How It Works](#how-it-works)
  * [Data Flow](#data-flow)
* [Scope of Improvement](#scope-of-improvement)
* [Acknowledgements](#acknowledgements)


## Introduction

### Newspip
Newspip is an end-to-end Natural Language Processing (NLP) pipeline for predicting stock price inflections by comparing the performance of supervised classification models (Naive Bayes, SVM) on financial news scraped from Reuters. 
This pipeline has been built flexibly to account for any stock that you want to track (provided company news articles are available on Reuters).
  
### Use Cases
Some use cases of this pipeline are 
  <li>Improve the accuracy of stock forecasting models that rely solely on the historic price feature</li>
  <li>Understand the correlation between a company's media perception and stock price inflection</li>
   

### Built With
* [Python](https://www.python.org/)
* [Selenium](https://selenium-python.readthedocs.io/)
* [Scikit-Learn](https://scikit-learn.org/stable/)
* [NLTK](https://www.nltk.org/)
* [Jupyter Notebook](https://jupyter.org/)
* [My Only Two Brain Cells](https://www.bbc.com/news/uk-england-sussex-36443264#:~:text=Snails%20use%20two%20brain%20cells,it%20if%20food%20was%20present.)


## How It Works
The pipeline currently has two classification models — Naive Bayes and SVM. Adding more classifiers can be done easily in "sentiment_analysis.ipynb". It compares the stock behavior forecast based on
<li>News article headlines</li>
<li>News article headlines + first sentence of the article as displayed on Reuters</li> 

Data is scraped from Reuters, cleaned, and then fitted with models.

### Data Flow
<ol>
  <li>
    <h4>Data Collection</h4>
   The dataset containing the company news (headlines, first sentences) is scraped from <a href="[https://www.reuters.com/](https://www.reuters.com/)">Reuters</a> using Selenium (refer "scrapers/").
   </li>
   <br>
   <li>
	   <h4>Data Cleaning</h4>
	   This is the second step in the pipeline. Common text processing/cleaning techniques are used to convert the dataset into a usable format (refer "pipeline/data_cleaning.ipynb").
	</li>
	<br>
	<li>
		<h4>Exploratory Analysis</h4>
		The cleaned dataset is then explored. Some of its features are visualized to verify if there are any direct correlations/patterns that can be derived (refer "pipeline/exploratory_analysis.ipynb").
  </li>
  <br>
  <li>
	  <h4>Sentiment Analysis</h4>
	  This is the final step in the pipeline where multiple models are fitted on the dataset to compare predictions. There's room for expansion at this stage. Since the previous steps have been abstracted away to accommodate any stock, you can only focus on model building/optimizing without having to worry about data collection and cleaning (refer "pipeline/sentiment_analysis.ipynb"). 
	  </li>
</ol>
  
## Scope of Improvement
<li>Adding more classification models</li>
<li>Optimizing the existing models</li>
<li>Increasing model performance by scraping more data</li>


## Acknowledgements
* [Infinite Scrolling in Selenium](https://dev.to/hellomrspaceman/python-selenium-infinite-scrolling-3o12)
* [Opening New Tab in Selenium](https://medium.com/@pavel.tashev/python-and-selenium-open-focus-and-close-a-new-tab-4cc606b73388)
* [Sentiment Analysis](https://medium.com/analytics-vidhya/natural-language-processing-from-scratch-sentiment-analysis-e09711d4f7eb)
* [SVM](https://medium.com/@vasista/sentiment-analysis-using-svm-338d418e3ff1)


##
<small><i>Note that this pipeline is flexible and the focus is not the accuracy of the models, but rather the room for extension so you can optimize the existing models and/or add new models.</i></small>
