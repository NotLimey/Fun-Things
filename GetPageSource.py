import requests
from bs4 import BeautifulSoup

URL = input("Type in url: ")
page = requests.get(URL, timeout=5);

soup = BeautifulSoup(page.content, "html.parser")

print(soup.prettify())