from bs4 import BeautifulSoup
from requests import get

URL = 'https://www.olx.pl/d/nieruchomosci/mieszkania/sprzedaz/gdansk/'

def parse_price(price):
    parsed_price = price.replace(' ','').replace('zł', '').replace(',','.')
    return float(parsed_price)

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

for offer in bs.find_all('div', class_='css-19ucd76'):
    try:
        location = offer.find('p', class_='css-p6wsjo-Text eu5v0x0').get_text().strip().split('-')[0]
        title = offer.find('h6', class_='css-v3vynn-Text eu5v0x0').get_text().strip()
        price = parse_price(offer.find('p', class_='css-wpfvmn-Text eu5v0x0').get_text().strip())
    except:
        continue

    print(location, title, price)
