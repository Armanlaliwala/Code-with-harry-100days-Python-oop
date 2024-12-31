import requests
from bs4 import BeautifulSoup

url = "http://laliwalait.com/"
r =requests.get(url)
print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify()) #this sow the output in a proper manner 

for heading in soup.find_all("h1"):
    print(heading.text)