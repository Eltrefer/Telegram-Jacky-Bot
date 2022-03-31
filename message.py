import json
import telebot
from telebot import REPLY_MARKUP_TYPES, types
import random
from parse360tech import Parse 

def Parsing(bot, text):
  bot.send_message(text.chat.id, Parse() )

def PN(bot, text):
    bot.send_message(text.chat.id, (
    'Понедельник на следующей неделе:'
    '\n-2 (практ.) Философия a. 2-510 доц. Борецкая Виктория Казимировна 10.00-11.25'
    '\n-3 (практ.) [КТвПЭ](http://www.example.com/) a. 2-542 доц. Ковалев А. В. 11.35-13.00'
    '\n-4 (лекц.) Математический анализ a. 2-542 доц. Евтухова Светлана Михайловна 13.30-14.55'
    '\n-5 (лаб.) КТвПЭ a. 2-540 доц. Ковалев А. В. 15.05-16.30'), parse_mode='Markdown'
    )

def NewAnswer(bot, text):
    img = open('E:\Files\Screnshots\Screenshot_1.png', 'rb')

    bot.send_photo(text.chat.id, img)
    bot.send_message(text.chat.id, "Товары для продажи\n#ItNetwork")

def Menu(bot, text):

    

    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)

    menu.add(
    types.KeyboardButton('ПН'),
    types.KeyboardButton('Саня'),
    types.KeyboardButton('Random'),
    types.KeyboardButton('Аниме'),
    types.KeyboardButton('Parsing'),
    types.KeyboardButton('Назад'))

    bot.send_message(text.chat.id, 'Понял', reply_markup=menu)


def start(bot, text):
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)

    start.add(
    types.KeyboardButton('Меню'),
    types.KeyboardButton('Пока'))

    sti = open('E:\Files\Py\JackyBOT\scr\AnimatedSticker_2.tgs', 'rb')
    bot.send_animation(text.chat.id, sti)
    bot.send_message(text.chat.id, 'Ну привет, сладкий'.format(text.from_user, bot.get_me()) , reply_markup=start)


def backMenu(bot, text):
    start1 = types.ReplyKeyboardMarkup(resize_keyboard=True)

    start1.add(
    types.KeyboardButton('Меню'),
    types.KeyboardButton('Пока'))

    bot.send_message(text.chat.id, 'Хорошо', reply_markup=start1)


def randomNumber(bot, text):
    bot.send_message(text.chat.id, str(random.randint(0, 5)))


def anime(bot, text):
    animeShit = open('E:/Files/Py/JackyBOT/scr/Ded_musul.mp4', 'rb')
    bot.send_animation(text.chat.id, animeShit)


def bye(bot, text):
    bot.send_message(text.chat.id, "Пей чай, пеки булки. Покеда")