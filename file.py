# Create a new virtual environment
# python -m venv .\wikipedia_scraper_env

# Import the requests library (1 line)
import requests

# Connect to the endpoint
# Assign the root url (without /status) to the root_url variable for ease of reference (1 line)
root_url = "https://country-leaders.onrender.com"
# Assign the /status endpoint to another variable called status_url (1 line)
status_url = "https://country-leaders.onrender.com/status"
# Query the /status endpoint using the get() method and store it in the req variable (1 line)
req = requests.get(status_url)

# Print response if successfull
if req.status_code == 200:
    print(req)
# Print status code if failed
else:
    print(req.status_code)

# Set the countries_url variable (1 line)
countries_url = "https://country-leaders.onrender.com/countries"
# Query the /countries endpoint using the get() method and store it in the req variable (1 line)
req = requests.get(countries_url)
# Get the JSON content and store it in the countries variable (1 line)
countries = ""
# Display the request's status code and the countries variable (1 line)
print(req.status_code, countries)

