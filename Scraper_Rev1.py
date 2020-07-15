import requests
from bs4 import BeautifulSoup

site = requests.get("https://isslive.com/displays/adcoDisplay1.html")
print(site.status_code)
if site.status_code == 200:

    src = site.content
    soup = BeautifulSoup(src,'lxml')
    print("The website is up and running at the moment \nHere is the website header:\n")
    print(site.headers)

else:
    print("Looks like that domain isn't active at the moment. \n \n A. The website could be either down \n B. The Domain Name is invalid or may have changed.")