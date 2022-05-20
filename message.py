import json
import telebot
from telebot import REPLY_MARKUP_TYPES, types
import random

def Menu(bot, text):

    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)

    menu.add(
    types.KeyboardButton('Аниме'),
    types.KeyboardButton('Parsing'),
    types.KeyboardButton('Назад'))

    bot.send_message(text.chat.id, 'Понял', reply_markup=menu)


def start(bot, text):
    start = types.ReplyKeyboardMarkup(resize_keyboard=True)

    start.add(
    types.KeyboardButton('Меню'),
    )

    sti = open('./scr/AnimatedSticker_2.tgs', 'rb')
    bot.send_animation(text.chat.id, sti)
    bot.send_message(text.chat.id, 'Ну привет, сладкий'.format(text.from_user, bot.get_me()) , reply_markup=start)


def backMenu(bot, text):
    start1 = types.ReplyKeyboardMarkup(resize_keyboard=True)

    start1.add(
    types.KeyboardButton('Меню'),
    )

    bot.send_message(text.chat.id, 'Хорошо', reply_markup=start1)


def anime(bot, text):
    animeShit = open('./scr/Ded_musul.mp4', 'rb')
    bot.send_animation(text.chat.id, animeShit)
