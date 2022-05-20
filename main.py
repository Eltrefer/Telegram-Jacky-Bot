from telebot.util import deprecated
import telebot

import message
from tech360 import Parse 

import config


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def answer(answ):
    message.start(bot, answ)


@bot.message_handler(content_types= ['text'])
def reply(replyText):


  if replyText.chat.type == 'private':


    if replyText.text == 'Parsing':
      Parse(bot, replyText)


    elif replyText.text == 'Меню':
        message.Menu(bot, replyText)


    elif replyText.text == 'Назад':
        message.backMenu(bot, replyText)


    elif replyText.text == 'Аниме':
        message.anime(bot,replyText)


    else:
        bot.send_message(replyText.chat.id, 'Unknown command. Try /start')



bot.polling(non_stop = True)
