from typing import Text
import telebot
import pymorphy2
import dict
import re
import time
from telebot import types

morph = pymorphy2.MorphAnalyzer(lang='ru')

telebot.apihelper.ENABLE_MIDDLEWARE = True

bot = telebot.TeleBot("5042716699:AAG0tctsEL_zJaVY0PNUSSwNVJA4cfOVouo")


@bot.message_handler(content_types=['photo', 'voice', 'audio', 'video', 'location', 'contact', 'sticker'])
def handle_docs_audio(message):
    bot.reply_to(message, 'Я вас не понимаю :(')


@bot.message_handler(commands=["help"])
def help_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/start')
    item2 = types.KeyboardButton('/help')
    item3 = types.KeyboardButton('/ask')
    item4 = types.KeyboardButton('/cordon')
    item5 = types.KeyboardButton('/faq')

    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, dict.thisdict["item1"].format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=["ask"])
def ask_message(message: telebot.types.Message):
    bot.reply_to(message, 'Задайте свой вопрос')

    @bot.message_handler(content_types=["text"])
    def askinner_message(message):
        words = message.text
        words = words.replace("?", "").split(" ")
        phrase=[]
        for word in words:
            word = morph.parse(word)[0].normal_form  # морфируем слово вопроса в нормальную словоформу
            phrase.append(word)
        answer = ''
        for i in phrase:
            for key, value in dict.thisdict.items(): 
                arrKey = key.split(' ')
                for k in arrKey:
                    if k == i:
                        answer = value
                        break
        if answer == '':
            bot.reply_to(message, '''Извините, я не смог найти ответа на ваш вопрос. Не могли бы вы перефразировать вопрос?''')
            return 
        else:
            bot.reply_to(message, answer)
            return
    return


@bot.message_handler(commands=['start'])
def start_message(message: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/start')
    item2 = types.KeyboardButton('/help')
    item3 = types.KeyboardButton('/ask')
    item4 = types.KeyboardButton('/faq')
    markup.add(item1, item2, item3, item4)
    text = dict.thisdict["item2"].format(message.from_user)
    bot.send_message(message.chat.id, text, reply_markup=markup)
    bot.reply_to(message, 'Если вы готовы начать, введите команду /step1')

    @bot.message_handler(commands=['step1'])
    def step1_message(message: telebot.types.Message):
        bot.reply_to(message, dict.thisdict["item3"])
        bot.reply_to(message, 'Если вы заполнили форму, введите команду /step2')

        @bot.message_handler(commands=['step2'])
        def step2_message(message: telebot.types.Message):
            bot.reply_to(message, dict.thisdict["item4"])
            bot.reply_to(message, 'Если вы зарегистрировались на сайте, введите команду /step3')

            @bot.message_handler(commands=['step3'])
            def step3_message(message: telebot.types.Message):
                bot.reply_to(message, dict.thisdict["item5"])
                bot.reply_to(message, 'Если вы отправили которкое видео о себе, введите команду /step4')

                @bot.message_handler(commands=['step4'])
                def step4_message(message: telebot.types.Message):
                    bot.reply_to(message, dict.thisdict["item6"])
                    bot.reply_to(message, 'Если готовы перейти к следующему шагу, введите команду /step5')

                    @bot.message_handler(commands=['step5'])
                    def step5_message(message: telebot.types.Message):
                        bot.reply_to(message, dict.thisdict["item7"])
                        bot.reply_to(message, 'Если вы отправили справку о прохождении медицинской комиссии и туристическую страховку, введите команду /step6')

                        @bot.message_handler(commands=['step6'])
                        def step6_message(message: telebot.types.Message):
                            bot.reply_to(message, dict.thisdict["item8"])
                            bot.reply_to(message, 'Если вы получили положительное решение по заявке, введите команду /step7')
                            
                            @bot.message_handler(commands=['step7'])
                            def step7_message(message: telebot.types.Message):
                                bot.reply_to(message, dict.thisdict["item9"])

                                bot.reply_to(message, dict.thisdict["item10"])


@bot.message_handler(commands=['cordon'])
def cordon_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/cordon1')
    item2 = types.KeyboardButton('/cordon2')
    item3 = types.KeyboardButton('/cordon3')
    item4 = types.KeyboardButton('/cordon4')
    item5 = types.KeyboardButton('/cordon5')
    item6 = types.KeyboardButton('/cordon6')
    item0 = types.KeyboardButton('/help')
    markup.add(item1, item2, item3, item4, item5, item6, item0)
    bot.send_message(message.chat.id, dict.thisdict["item11"].format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['cordon1'])
def cordon1_message(message: telebot.types.Message):    
    bot.reply_to(message, dict.thisdict["item12"])
    bot.reply_to(message, dict.thisdict["item13"])


@bot.message_handler(commands=['cordon2'])
def cordon2_message(message: telebot.types.Message):    
    bot.reply_to(message, dict.thisdict["item14"])
    bot.reply_to(message, dict.thisdict["item15"])


@bot.message_handler(commands=['cordon3'])
def cordon3_message(message: telebot.types.Message):
    bot.reply_to(message, dict.thisdict["item16"])
    bot.reply_to(message, dict.thisdict["item17"])


@bot.message_handler(commands=['cordon4'])
def cordon4_message(message: telebot.types.Message):
    bot.reply_to(message, dict.thisdict["item18"])
    bot.reply_to(message, dict.thisdict["item19"])


@bot.message_handler(commands=['cordon5'])
def cordon5_message(message: telebot.types.Message):
    bot.reply_to(message, dict.thisdict["item20"])
    bot.reply_to(message, dict.thisdict["item21"])


@bot.message_handler(commands=['cordon6'])
def cordon6_message(message: telebot.types.Message):
    bot.reply_to(message, dict.thisdict["item22"])


@bot.message_handler(commands=['faq'])
def faq_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/food')
    item2 = types.KeyboardButton('/living')
    item3 = types.KeyboardButton('/graphic')
    item4 = types.KeyboardButton('/prepare')
    item5 = types.KeyboardButton('/connectivity')
    item6 = types.KeyboardButton('/contract')
    item7 = types.KeyboardButton('/departure')
    item8 = types.KeyboardButton('/waiting')
    item9 = types.KeyboardButton('/jobs')
    item10 = types.KeyboardButton('/report')
    item0 = types.KeyboardButton('/help')

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item0)
    bot.send_message(message.chat.id, dict.thisdict["item23"].format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['food'])
def food_message(message: telebot.types.Message):
    bot.reply_to(message, dict.thisdict['питание еда кафе рестораны кушать питаться поесть'])


@bot.message_handler(commands=['living'])
def living_message(message: telebot.types.Message):
    bot.reply_to(message, dict.thisdict['проживание условие условия отели ночевка дом жилье жить спать переночевать жить'])


@bot.message_handler(commands=['graphic'])
def graphic_message(message: telebot.types.Message):
    bot.reply_to(message, dict.thisdict['график срок'])


@bot.message_handler(commands=['prepare'])
def prepare_message(message: telebot.types.Message):
    bot.reply_to(message, dict.thisdict['подготовка путешествие взять'])


@bot.message_handler(commands=['connectivity'])
def connectivity_message(message: telebot.types.Message):
    bot.reply_to(message, dict.thisdict['связь электричество интернет'])


@bot.message_handler(commands=['contract'])
def contract_message(message: telebot.types.Message):
    bot.reply_to(message, dict.thisdict['подписать договор соглашение'])


@bot.message_handler(commands=['departure'])
def departure_message(message: telebot.types.Message):
    bot.reply_to(message, dict.thisdict['отправка отправление когда'])


@bot.message_handler(commands=['waiting'])
def waiting_message(message: telebot.types.Message):
    bot.reply_to(message, dict.thisdict['ожидание отправка'])


@bot.message_handler(commands=['jobs'])
def jobs_message(message: telebot.types.Message):
    bot.reply_to(message, dict.thisdict['работа заниматься обязанность выполнять делать'])


@bot.message_handler(commands=['report'])
def report_message(message: telebot.types.Message):
    bot.reply_to(message, dict.thisdict['отзыв отчет'])


bot.polling(none_stop=True)
