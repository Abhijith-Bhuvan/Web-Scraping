import requests
from bs4 import BeautifulSoup as bs


page = requests.get('https://www.worldometers.info/coronavirus/')
soup = bs(page.text, 'html.parser')

table = soup.find('table', attrs={'id': 'main_table_countries_today'})
table_body = table.find('tbody')

rows = table_body.findAll('tr')

for row in rows:
    print(row.contents)
