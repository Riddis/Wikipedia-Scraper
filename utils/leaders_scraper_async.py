import asyncio
import aiohttp
import json
import re
from bs4 import BeautifulSoup as soup
import requests

def get_leaders():
    """Loops through and returns all the leaders per country"""
    cookie_url = "https://country-leaders.onrender.com/cookie"
    countries_url = "https://country-leaders.onrender.com/countries"
    leaders_url = "https://country-leaders.onrender.com/leaders"
    leaders_per_country = {}

    # Create a global session for all our requests
    session = requests.Session() 

    # Get a cookie
    cookies=(session.get(cookie_url)).cookies
    # Get the list of countries
    countries = (session.get(countries_url, cookies=cookies)).json()
    # Loop through the list of countries and get their leaders
    for country in countries:
        url = leaders_url+"?country="+country
        leaders_per_country[country] = (session.get(url, cookies=cookies)).json()

    # Return the list of leadders per country
    return leaders_per_country

async def get_wikipedia_info(url, session, countries, leaders):
    async with session.get(url) as resp:
        info = await resp.text()
        return (countries, leaders, info)

async def session_loop_request_async(leaders_per_country):
    # Create shared session for all your requests
    async with aiohttp.ClientSession() as session:
        # Create a list of empty tasks
        tasks = []

        # Loop through countries
        for country, leaders in leaders_per_country.items():
            # Loop through leaders per country
            for leader in leaders:
                # Get the Wikipedia entry
                url = leader['wikipedia_url']
                # Add a request to tasks
                tasks.append(get_wikipedia_info(url, session, country, leader))

        # Now that all the tasks are registered, run them
        responses = await asyncio.gather(*tasks)
    return responses

def get_first_paragraph(responses):
    """Fetches the first paragraph of Wikipedia and sanitizes the output to a readable format"""
    leaders_per_country = {}

    # Loop through responses
    for countries, leaders, response in responses:
        wikipedia = soup(response, 'html.parser')
        # Get all paragraphs on the page
        for p in wikipedia.find_all('p'):
            # Find the first paragraph and clean it up
            if re.match("(^<p><b>(.*?)<\/b>)", str(p)):
                # Cleanup file
                paragraph = re.sub("<.*?>|\(?\/.*?\;|\[.\]|\[.*\](\[.*\])?|\\n|.\(background(.*?)couter\).|\.(\(?)\.mw(.*?)couter\).| ? .mw(.*?)couter.| Dutch pronunciation: (\[.*\])? ;|\(? ?uitspraak|\(info \/ uitleg\)\)?", "", str(p))
                paragraph = re.sub("( ){2,}", " ", str(paragraph.strip()))
                leaders['info'] = paragraph
                leaders_per_country.setdefault(countries, []).append(leaders)
                # First paragraph has been found, stop the loop
                break

    return leaders_per_country

def save(leaders):
    """Saves a JSON file to './data_async.json'"""
    with open('./data_async.json', 'w') as file:
        json.dump(leaders, file)