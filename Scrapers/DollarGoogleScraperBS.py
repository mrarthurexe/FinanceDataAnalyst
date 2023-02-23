__package__ = "Finance.Scrapers"

from urllib.request import URLopener
from bs4 import BeautifulSoup
import collections
bsObj = BeautifulSoup(URLopener().open("https://www.google.com/finance/quote/USD-BRL?sa=X&ved=2ahUKEwiZi9bZ_aj9AhVKLbkGHQFcD1YQmY0JegQIBhAd").read(), "html.parser")
collections.Callable = collections.abc.Callable

def getValue():
    try:
        dollar = bsObj.find('div', {'class':"YMlKec fxKbKc"}).get_text()
        return dollar

    except Exception as e:
        print('Error collecting value:' + e)
        exit()

def getDate():
    try:
        date = bsObj.find('div', {'class':"ygUjEc"}).get_text()
        date = date.replace(' · Disclaimer', '')
        return date

    except Exception as e:
        print('Error collecting date:' + e)
        exit()