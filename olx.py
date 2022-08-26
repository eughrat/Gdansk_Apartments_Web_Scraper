from bs4 import BeautifulSoup
from requests import get
from olx_functions import parse_link, parse_price
import sqlite3
from sys import argv

def parse_page(number):
    page = get(f'{URL}&page={number}')
    bs = BeautifulSoup(page.content, 'html.parser')
    for offer in bs.find_all('div', class_='css-19ucd76'):
        try:
            location = offer.find('p', class_='css-p6wsjo-Text eu5v0x0').get_text().strip().split('-')[0]
            title = offer.find('h6', class_='css-v3vynn-Text eu5v0x0').get_text().strip()
            price = parse_price(offer.find('p', class_='css-wpfvmn-Text eu5v0x0').get_text().strip())
            link = parse_link(offer.find('a')['href'])
        except:
            continue
        cursor.execute('INSERT INTO offers VALUES (?, ?, ?)', (title, price, location))
    db.commit()

URL = 'https://www.olx.pl/d/nieruchomosci/mieszkania/sprzedaz/gdansk'
db = sqlite3.connect('dane.db')
cursor = db.cursor()

if len(argv) > 1 and argv[1] == 'setup':
    cursor.execute('''CREATE TABLE offers (name TEXT, price REAL, location TEXT) ''')
    quit()

for page in range(1,31):
    parse_page(page)

db.close()