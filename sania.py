from telebot import REPLY_MARKUP_TYPES, types

def Variants(bot, text):
    Menu = types.ReplyKeyboardMarkup(resize_keyboard=True)

    Menu.add(
    types.KeyboardButton('Саня, хуй соси'),
    types.KeyboardButton('Саня, сотку верни'),
    types.KeyboardButton('Саня, ты в порядке?'),
    types.KeyboardButton('Меню'))

    bot.send_message(text.chat.id, 'Что там с Саней?', reply_markup=Menu)


def Poriadok(bot, text):
    Poriadok = open('E:\Files\Py\JackyBOT\scr\SaniaPoriadok.mp3', 'rb')
    bot.send_audio(text.chat.id, Poriadok)#.format(text.from_user, bot.get_me()))    


def Sotka(bot, text):
    Sotka = open('E:\Files\Py\JackyBOT\scr\saniaSotka.jpg', 'rb')
    bot.send_photo(text.chat.id, Sotka, caption='ffgfg')
    caption= "sfh kdsf sd f"
    tt= 'aadf dd f'
    bot.send_message(text.chat.id, tt.caption)
    bot.send_message(text.chat.id, 'Я жду...'.format(text.from_user, bot.get_me()))


def Huy(bot, text):
    Huy = open('E:\Files\Py\JackyBOT\scr\sania.gif', 'rb')
    bot.send_animation(text.chat.id, Huy)


def Zaeb(bot, text):
    Zaeb = open('E:\Files\Py\JackyBOT\scr\Sania_zaeb.jpg', 'rb')
    bot.send_photo(text.chat.id, Zaeb)
