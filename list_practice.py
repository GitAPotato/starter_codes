import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com/")

print(result.status_code);
# 404 Means Not working
# 200 means ok
#if result.status_code == 200:

 #   print("\nLooks like the website you selected is up and running!\n")
 #   print(result.headers)

#else:
#    print("Looks like we can't find that domain. Maybe try using a different address?")

src = result.content
soup = BeautifulSoup(src, 'lxml')

