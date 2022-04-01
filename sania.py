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
    Poriadok = open('./scr/SaniaPoriadok.mp3', 'rb')
    bot.send_audio(text.chat.id, Poriadok)#.format(text.from_user, bot.get_me()))    


def Sotka(bot, text):
    Sotka = open('./scr/saniaSotka.jpg', 'rb')
    bot.send_photo(text.chat.id, Sotka, caption='Я жду...')
    # caption= "sfh kdsf sd f"
    # tt= 'aadf dd f'
    # bot.send_message(text.chat.id, tt.caption)
    # bot.send_message(text.chat.id, 'Я жду...'.format(text.from_user, bot.get_me() ) )


def Huy(bot, text):
    Huy = open('./scr/sania.gif', 'rb')
    bot.send_animation(text.chat.id, Huy)


def Zaeb(bot, text):
    Zaeb = open('./scr/Sania_zaeb.jpg', 'rb')
    bot.send_photo(text.chat.id, Zaeb)
