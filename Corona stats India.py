import requests
from bs4 import BeautifulSoup as bs


def get_stats_india():
    page = requests.get('https://www.worldometers.info/coronavirus/country/india/')

    soup = bs(page.text, 'html.parser')

    data = soup.findAll(class_='maincounter-number')
    numbers = {}

    numbers['Total Cases'] = str(data[0].contents[1].text)
    numbers['Total Deaths'] = str(data[1].contents[1].text)
    numbers['Total Recovered'] = str(data[2].contents[1].text)

    print('Corona stats of India')
    for key in numbers:
        print(key, ' : ', numbers[key])
    return numbers


if '__main__' == __name__:
    stats = get_stats_india()
