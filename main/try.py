import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.analyticsvidhya.com/blog/?utm_source=feed&utm_medium=navbar')

soup = BeautifulSoup(r.text, "html.parser")

# print(soup.prettify())
# for link in soup.find_all('a'):
#     c = link.get('title')
#     # print(type(c))
#     if type(c) is str:
# 	    print(c)


print(soup.find_all('a').get('title'))