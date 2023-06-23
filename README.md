# Your first scraper

- Repository: `Wikipedia Scrapper`
- Type of Challenge: `Learning`
- Time Spent: `2 days on the main project, half a day on the bonus async version`

- Team challenge : `Solo`

This project was done as part of the AI Boocamp at BeCode.org 

## The Mission

In this project, we will guide you step by step through the process of:

1. creating a self-contained development environment.
2. retrieving some information from an API (a website for computers)
3. leveraging it to scrape a website that does not provide an API
4. saving the output for later processing
5. as a bonus exercise, I also created an asynchronous version

Here we query an API for a list of countries and their past leaders. We then extract and sanitize their short bio from Wikipedia. Finally, we save the data to disk.

This task is often the first (coding) step of a datascience project and you will often come back to it in the future.

## Learning objectives

You will study topics such as *scraping*, *data structures*, *regular expressions*, *concurrency* and *file handling*. We will point out useful resources at the appropriate time. 

## Installation

You will need to install the following modules:

1. Requests
2. BeautifulSoup (bs4)
3. Aiohttp (bonus)

## Usage

You can run the synchronous script by running `python main.py` in the terminal
It will save the data in a .\data.json file

You can run the asynchronous script by running `python main_async.py` in the terminal
It will save the data in a .\data_async.json file

