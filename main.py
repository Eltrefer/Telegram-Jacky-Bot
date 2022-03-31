from telebot.util import deprecated
import telebot
import message
import sania

import config


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def answer(answ):
    message.start(bot, answ)


@bot.message_handler(content_types= ['text'])
def reply(replyText):


    if replyText.chat.type == 'private':


        if replyText.text == 'Parsing':
            message.Parsing(bot, replyText)


        if replyText.text == 'ПН':
            message.PN(bot, replyText)


        elif replyText.text == 'Меню':
            message.Menu(bot, replyText)


        elif replyText.text == 'Саня':
            sania.Variants(bot, replyText)


        elif replyText.text == 'Саня, ты в порядке?':
            sania.Poriadok(bot, replyText)
        

        elif replyText.text == 'Саня, сотку верни':
            sania.Sotka(bot, replyText)


        elif replyText.text == 'Саня, хуй соси':
            sania.Huy(bot, replyText)
            

        elif replyText.text == 'Назад':
            message.backMenu(bot, replyText)
        

        elif replyText.text == 'Пока':
            bot.send_message(replyText.chat.id, "Пей чай, пеки булки. Покеда")


        elif replyText.text == 'Random':
            message.randomNumber(bot, replyText)


        elif replyText.text == 'Аниме':
            message.anime(bot,replyText)


        elif replyText.text == '5':
            sania.Zaeb(bot, replyText)

        elif replyText.text == '111':
            message.NewAnswer(bot, replyText)


        else:
            bot.send_message(replyText.chat.id, 'Unknown command. Try /start')



bot.polling(non_stop = True)
