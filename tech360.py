import requests
from bs4 import BeautifulSoup
import telebot

# TOKEN = '1885649071:AAEAkbg16I0BICwkL90g8XfLFfOM0HfarQc'

def Parse(bot, text):
  
  url = 'https://www.techno360.in'
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'lxml')

  items = soup.find_all('div', class_="post-column clearfix")
  
  # result =

  for n, i in enumerate(items, start=1):

      itemName = i.find('h2', class_="entry-title").text.strip()
      itemDate = i.find('time', class_='entry-date published updated').text.strip()
      itemImage = ( i.find('img') )['src']

      result = ''.join([str(n), '. ', '[', itemDate, '] ', itemName, '\n'])
      bot.send_photo(text.chat.id, itemImage, caption=result )

      # if (type == 'text'):
      #   result += ''.join([str(n), '. ', '[', itemDate, '] ', itemName, '\n'])
      # elif (type == 'img'):
      #   result = itemImage

  # return result

# def Pars(bot, text):
#   bot.send_photo(text.chat.id, Parse("img"), caption=Parse('text') )
# bot = telebot.TeleBot(TOKEN)
# bot.send_photo(1460335592, Parse("img"), caption=Parse('text') )
