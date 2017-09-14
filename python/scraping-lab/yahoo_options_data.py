import json
import sys
import re
import urllib 
from bs4 import BeautifulSoup
import json
import re

def contractAsJson(filename):

  with open(filename) as fp:
      soup = BeautifulSoup(fp)

  currPrice = float(soup.find_all(class_='time_rtq_ticker')[0].span.text)
  dateUrls = []
  optionQuotes = []

  dateUrlTags = soup.select('#yfncsumtab')[0].select('a[href*=m=]')
  for d in dateUrlTags :
    dateUrls.append('http://finance.yahoo.com'+d['href'].replace('&','&amp;'))

  rows = soup.select('.yfnc_datamodoutline1 > tr > td > table > tr')
  for row in rows :
    cells = row.select('td')
    if len(cells) > 0:
      p = re.compile('(?P<symboldate>[A-Z]+\d+)(?P<type>[A-Z]+)\d+')
      m = p.search(cells[1].text)
      
      change = cells[3].text
      if len(cells[3].select('img[alt=Up]')) > 0 :
        change = change.replace(' ','+')
      elif len(cells[3].select('img[alt=Down]')) > 0:
        change = change.replace(' ', '-')

      optionQuotes.append({
        'Strike': cells[0].text,
        'Symbol': m.group('symboldate')[0:len(m.group('symboldate'))-6],
        'Type': m.group('type'),
        'Date': m.group('symboldate')[len(m.group('symboldate'))-6:len(m.group('symboldate'))],
        'Last': cells[2].text,
        'Change': change,
        'Bid': cells[4].text,
        'Ask': cells[5].text,
        'Vol': cells[6].text,
        'Open': cells[7].text
        })
      
      optionQuotes = sorted(optionQuotes,key=lambda x: float(x['Open'].replace(',','')),reverse=True)

  return json.dumps({'currPrice':currPrice,'dateUrls':dateUrls,'optionQuotes':optionQuotes},indent=4,sort_keys=True,separators=(',',': '))

