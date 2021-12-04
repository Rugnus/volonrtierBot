import telebot
import pymorphy2
import dict
import re
import time
from telebot import types

morph = pymorphy2.MorphAnalyzer(lang='ru')

telebot.apihelper.ENABLE_MIDDLEWARE = True

bot = telebot.TeleBot("5042716699:AAG0tctsEL_zJaVY0PNUSSwNVJA4cfOVouo")

@bot.message_handler(commands=["help"])
def help_message(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/start')
    item2 = types.KeyboardButton('/help')
    item3 = types.KeyboardButton('/ask')

    murkup.add(item1, item2, item3)
    bot.send_message(message.chat.id, '''Привет, {0.first_name}, я Вио! Я создан для того, чтобы помочь волонтерам с этапами прохождения отбора и с часто задаваемыми вопросами. Все команды:
/start - начало прохождения этапа отбора 
/help - знакомство с Вио 
/ask - задайде вопрос'''.format(message.from_user), reply_markup = murkup)

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
            # Нормализуем словоформу каждого слова и соберем обратно фразу
            phrase.append(word)
        answer = ''
        for i in phrase:
            for key, value in dict.thisdict.items(): 
                arrKey = key.split(' ')
                for k in arrKey:
                    if k == i:
                        print('совпАЛООО')
                        answer = value
                        break
        if answer == '':
            bot.reply_to(message, '''Извините, я не смог найти ответа на ваш вопрос. Не могли бы вы перефразировать вопрос?''')
            return 
        else:
            bot.reply_to(message, answer)
            return 
    print('ask_message')
    return
print('main_ask_message')

@bot.message_handler(commands=['start'])
def start_message(message: telebot.types.Message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/start')
    item2 = types.KeyboardButton('/help')
    item3 = types.KeyboardButton('/ask')
    murkup.add(item1, item2, item3)
    text = '''Добрый день,{0.first_name}, меня зовут Вио! Далее будет проходить анкетирование, во время которого важно соблюдать порядок прохождения этапа. 
Все доступные команды:
/start - начало прохождения этапа отбора 
/help - знакомство с Вио 
/ask - задайде вопрос'''.format(message.from_user)
    bot.send_message(message.chat.id, text, reply_markup = murkup)
    bot.reply_to(message, 'Если вы готовы начать, введите команду /step1')

    @bot.message_handler(commands=['step1'])
    def step1_message(message: telebot.types.Message):
        text = '''От Вас поступил запрос о прохождении волонтерских работ на территории Кроноцкого государственного заповедника/Южно-Камчатского федерального заказника, для постановки в график Вам необходимо:
1) Заполнить анкету на прохождение обучения в Школе Защитников Природы, ссылка на форму анкеты: https://docs.google.com/forms/d/1idhdo4KswngdMijyXZWx_TXGWqJuKn7ySRzjeR0UnsI/edit;
2) Пройти курс, по окончании которого у Вас будет итоговый тест, в случае успешного результата Вас перенаправят в отдел познавательного туризма, далее Вы заполняете еще одну анкету (волонтера Кроноцкого заповедника) по утвержденной форме на сайте www.kronoki.ru, в разделе ВОЛОНТЕРСТВО,
в левом меню выбираем пункт ОФОРМИТЬ ЗАЯВКУ,
либо по ссылке, ссылка на форму анкеты: https://docs.google.com/forms/d/e/1FAIpQLSe1gyTpb69_1pNQPa3bFChFebvAfFMMDyBSWL9cUeRJqLSBWQ/viewform;
Прием заявок на 2022 год начинается с 05.12.2021 года
Обращаем внимание, что, заполняя форму, вы даете согласие на обработку персональных данных в соответствии с «Пользовательским соглашением» и «Политикой конфиденциальности».'''
        bot.reply_to(message, text)
        bot.reply_to(message, 'Если вы заполнили форму, введите команду /step2')

        @bot.message_handler(commands=['step2'])
        def step2_message(message: telebot.types.Message):
            text = '''Регистрация на сайте «Добровольцы России»- обязательна, ссылка на сайт: https://dobro.ru/.'''
            bot.reply_to(message, text)
            bot.reply_to(message, 'Если вы зарегистрировались на сайте, введите команду /step3')

            @bot.message_handler(commands=['step3'])
            def step3_message(message: telebot.types.Message):
                text = '''Заявок всегда в десятки раз больше, чем мест. Мы тщательно отбираем волонтеров, учитываем их образование, профессию, наличие рекомендаций от других заповедников и личные качества.Дистанционно выбрать подходящего человека бывает сложно,
поэтому мы рады, когда вы сопровождаете заявки короткими видео о себе (на 1-2 минуты).'''
                bot.reply_to(message, text)
                bot.reply_to(message, 'Если вы отправили которкое видео о себе, введите команду /step4')

                @bot.message_handler(commands=['step4'])
                def step4_message(message: telebot.types.Message):
                    text = '''Вам необходимо предоставить рекомендации, благодарности по итогам участия в волонтерских акциях и проектах (при наличии).
Приветствуется наличие личной книжки волонтёра'''
                    bot.reply_to(message, text)
                    bot.reply_to(message, 'Если готовы перейти к следующему шагу, введите команду /step5')

                    @bot.message_handler(commands=['step5'])
                    def step5_message(message: telebot.types.Message):
                        text = '''При наличии, просьба предоставить справки о прохождении медицинской комиссии, если проходили в течение последнего года, или предоставить расписку о состоянии здоровья (ограничения, хронические заболевания)
Предоставить туристическую страховку.'''
                        bot.reply_to(message, text)
                        bot.reply_to(message, 'Если вы отправили справку о прохождении медицинской комиссии и туристическую страховку, введите команду /step6')

                        @bot.message_handler(commands=['step6'])
                        def step6_message(message: telebot.types.Message):
                            text = '''После получения подтверждения отбора Вашей кандидатуры, при постановке в график, учитываются Ваши пожелания по территориям ООПТ для осуществления добровольческой деятельности.
В случае если график групп на данную территорию переполнен, Вам будет предложена другая территория, при наличии свободных мест.
Ознакомиться с актуальным графиком набора волонтеров можно на сайте www.kronoki.ru, либо по ссылке https://kronoki. ru/ru/volunteerism/programs/
При положительном решении, Вы получаете от нас письмо с приложениями:
договор о добровольческой деятельности для ознакомления:
    • с техническим заданием
    • с согласием на обработку персональных данных 
    • правилами нахождения на территории.'''
                            bot.reply_to(message, text)
                            bot.reply_to(message, 'Если вы получили положительное решение по заявке, введите команду /step7')
                            
                            @bot.message_handler(commands=['step7'])
                            def step7_message(message: telebot.types.Message):
                                text = '''Внимательно изучив все пункты договора и его приложений, Вы высылаете нам скан-копию подписанного документа'''
                                bot.reply_to(message, text)

                                bot.reply_to(message, '''Если вы хотите вернуться к предыдущим этапам, вы можете ввести команды: 
/start - начало этапа 
/step1 - первый этап: подача заявки 
/step2 - второй этап: регистрация на сайте «Добровольцы России»
/step3 - третий этап: запись и отправка короткого видео о себе
/step4 - четвертый этап: рекомендации, благодарности, наличие личной книжки волонтёра
/step5 - пятый этап: справки о медицинской комиссии, туристическая страховка 
/step6 - шестой этап: договор о добровольческой деятельности для ознакомления
/step7 - седьмой этап: скан-копия подписанного договора.

Если у вас еще остались ещё вопросы, вы можете их задать мне. Буду рад вам помочь. Ваш Вио!  ''')
                                #тут вывести все команды 
                                #тут @bot.message_handler(content_types=["text"])          
#задачи:                                
# придумать куда отправлять данные пользователя
bot.polling(none_stop=True)
