from xml.etree.ElementTree import tostring
import requests
from bs4 import BeautifulSoup

def Parse():
  
  url = 'https://www.techno360.in'
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'lxml')

  items = soup.find_all('header', class_="entry-header")
  
  result = ''

  for n, i in enumerate(items, start=1):

      itemName = i.find('h2', class_="entry-title").text.strip()
      itemDate = i.find('time', class_='entry-date published updated').text.strip()

      result += ''.join([str(n), '. ', '[', itemDate, '] ', itemName, '\n'])

  return result