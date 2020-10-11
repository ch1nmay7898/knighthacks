import requests
from bs4 import BeautifulSoup
import re


URL = 'https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=gmanju&btnG='
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='gs_ai_cby')
print(results.prettify().splitlines()[1].split()[2])
"""
edomain = re.search("\w+", "Chinmay Agrawal").group(0)

print(edomain)
"""