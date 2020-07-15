# YouTube Link:

# Ensure that you have both beautifulsoup and requests installed:
#   pip install beautifulsoup4
#   pip install requests

import requests
from bs4 import BeautifulSoup

# Using the requests module, we use the "get" function
# provided to access the webpage provided as an
# argument to this function:
result = requests.get("https://www.google.com/")

# To make sure that the website is accessible, we can
# ensure that we obtain a 200 OK response to indicate
# that the page is indeed present:
print(result.status_code)

# For other potential status codes you may encounter,
# consult the following Wikipedia page:
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# We can also check the HTTP header of the website to
# verify that we have indeed accessed the correct page:
print(result.headers)
