def get_leaders():
    """Loops through and returns all the leaders per country"""
    import requests
    # Set important URLs
    cookie_url = "https://country-leaders.onrender.com/cookie"
    countries_url = "https://country-leaders.onrender.com/countries"
    leaders_url = "https://country-leaders.onrender.com/leaders"
    leaders_per_country = {}
    # Create a global session for all our requests
    global session  
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

def get_first_paragraph():
    """Fetches the first paragraph of wikipedia and sanitizes the output to a readable format"""
    from bs4 import BeautifulSoup as soup
    import re

    # Get all leaders
    leaders_per_country = get_leaders()
    # Loop through countries
    for countries in leaders_per_country:
        #Loop through leaders per country
        for leaders in leaders_per_country[countries]:
            # Get the wikipedia entry
            url = leaders['wikipedia_url']
            # Get the leader's wikipedia page
            url = session.get(url).text
            wikipedia = soup(url, 'html.parser')
            # Get all paragraphs on the page
            for p in wikipedia.find_all('p'):
                # Find the first paragraph and clean it up
                if re.match("(^<p><b>(.*?)<\/b>)", str(p)):
                    # remove tags
                    first_paragraph = re.sub("<.*?>", "", str(p))
                    # remove phonetics
                    first_paragraph = re.sub("\(?\/.*?\;", "(", str(first_paragraph))
                    # remove [n]
                    first_paragraph = re.sub("\[.\]", "", str(first_paragraph))
                    first_paragraph = re.sub("\[.*\](\[.*\])?", "", str(first_paragraph))
                    # remove trailing \n
                    first_paragraph = re.sub("\\n", "", str(first_paragraph))
                    # remove various strings
                    first_paragraph = re.sub(".\(background(.*?)couter\).", "", str(first_paragraph))
                    first_paragraph = re.sub(".(\(?)\.mw(.*?)couter\).", "", str(first_paragraph))
                    first_paragraph = re.sub(" ? .mw(.*?)couter.", "", str(first_paragraph))
                    first_paragraph = re.sub(" Dutch pronunciation: (\[.*\])? ;", "", str(first_paragraph))
                    first_paragraph = re.sub("\(? ?uitspraak", "", str(first_paragraph))
                    first_paragraph = re.sub("\(info \/ uitleg\)\)?", "", str(first_paragraph))
                    # Remove extra whitespaces
                    first_paragraph = re.sub("( ){2,}", " ", str(first_paragraph)) # Not working for some reason :'(
                    leaders['info'] =  first_paragraph
                    # First paragraph has been found, stop the loop
                    break 
    return leaders_per_country

def save (leaders):
    """Saves a JSON file to .\data.json"""
    import json
    with open('.\data.json', 'w') as file:
        json.dump(leaders, file)