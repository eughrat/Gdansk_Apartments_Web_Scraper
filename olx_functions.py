from bs4 import BeautifulSoup
import sqlite3

def parse_price(price):
    parsed_price = price.replace(' ','').replace('zł', '').replace(',','.')
    return float(parsed_price)

def parse_link(link):
    if link[0:4] == 'http':
        return link
    else:
        return 'https://www.olx.pl' + link
