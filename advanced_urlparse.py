from requests import get
from csv import DictReader
from bs4 import BeautifulSoup as Soup
from datetime import date
from io import StringIO

SECURITY_NAME="3MINDIA" # Change this to get quote for another stock
START_DATE= date(2017, 1, 1) # Start date of stock quote data DD-MM-YYYY
END_DATE= date(2017, 9, 14)  # End date of stock quote data DD-MM-YYYY


BASE_URL = "https://streambet.cc/slots/sr_aviator?mode=demo"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Referer': 'https://cssspritegenerator.com',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}


def getquote(symbol, start, end):
    start = start.strftime("%-d-%-m-%Y")
    end = end.strftime("%-d-%-m-%Y")
    url = BASE_URL.format(security=symbol, start_date=start, end_date=end)
    d = get(url, headers=hdr)
    soup = Soup(d.content, 'html.parser')
    payload = soup.find('div', {'id': 'csvContentDiv'}).text.replace(':', '\n')
    csv = DictReader(StringIO(payload))
    for row in csv:
        a = 0
        return ({k:v.strip() for k, v in row.items()})

 if __name__ == '__main__':
     getquote(SECURITY_NAME, START_DATE, END_DATE)