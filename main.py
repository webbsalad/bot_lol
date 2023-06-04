import random
import telebot
import time
from telebot import types

from config import bot_api, admin_code

bot = telebot.TeleBot(bot_api)


class Actions:
    def __init__(self, name, act):
        self.name = name
        self.act = act


a = []


# стартовая комманда + появление кнопок
@bot.message_handler(commands=['start'])
def start(message):
    mess = 'Привет, ' + str(message.from_user.first_name) + '!'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(1363681575, (str(message.from_user.first_name) + ' Зашел'), parse_mode='html')
    print(message.from_user.first_name, 'ЗАШЁЛ')
    nkey = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key2 = types.KeyboardButton('История🎭')
    key4 = types.KeyboardButton('Состав группы👨‍👨‍👦')
    key3 = types.KeyboardButton('Перспективы😎')
    key1 = types.KeyboardButton('Тема работы🥼')
    key5 = types.KeyboardButton('Полезности🧩')
    keyl = types.KeyboardButton('НЕТ😵😵')

    nkey.add(key1, key2, key3, key4, key5, keyl)

    bot.send_message(message.chat.id,
                     'Я <b>бот</b>, созданный для демонстрации работы других ботов. (ну и там защиту сделать...)',
                     parse_mode='html', reply_markup=nkey)


@bot.message_handler(commands=['stp'])
def stop_command(message):
    print('\nпрограмма остановилось')
    bot.stop_polling()


# поманда помощи
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Бог поможет🙏🏻', parse_mode='html')
    bot.send_message(1363681575, (str(message.from_user.first_name) + ' взывает о помощи'), parse_mode='html')
    a.append(Actions(message.from_user.first_name, 'взывает о помощи'))
    print(str(message.from_user.first_name) + ' взывает о помощи')


# реакция на стикер
@bot.message_handler(content_types=['sticker'])
def sti(message):
    lis = ['Крутой стрикер', 'Ну неплохо', 'вау', '😀', 'чел...', 'dies from cringe😵',
           '(тут абсолютно случайная оценка т.ч не стоит увлекаться)']
    bot.send_message(message.chat.id, random.choice(lis), parse_mode='html')
    bot.send_message(1363681575, (str(message.from_user.first_name) + ' отправил стикер'), parse_mode='html')
    a.append(Actions(message.from_user.first_name, 'отправил стикер'))
    print(str(message.from_user.first_name) + ' отправил стикер')


# кнопки и сообщения
@bot.message_handler(content_types=['text'])
def fif(message):
    mes1 = str(message.from_user.first_name)
    if message.text == 'Состав группы👨‍👨‍👦':
        bot.send_message(message.chat.id, 'Суворов Роман🌈 \n Гневнов Артем🐸 \n Адаменко Семён🤖', parse_mode='html')
        mes2 = 'Состав группы'

    elif message.text == 'История🎭':
        bot.send_message(message.chat.id,
                         'Ро́бот, или бот, а также интернет-бот и тому подобное — специальная программа, выполняющая '
                         'автоматически и/или по заданному расписанию какие-либо действия через интерфейсы, '
                         'предназначенные для людей.',
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         'В 1950 году Алан Тьюринг, пионер компьютеров, написал научную статью «Вычислительные машины '
                         'и интеллект». В статье ученый имел в виду, что компьютерная программа может думать и '
                         'говорить как человек. Чтобы доказать это, Тьюринг предложил эксперимент под названием '
                         '«Имитационная игра», который сегодня известен как тест Тьюринга. Тьюринг полагал, '
                         'что к 2020 году машины смогут легко пройти его испытания.',
                         parse_mode='html')
        bot.send_message(message.chat.id,
                         'Элиза — первый чат-бот В 1966 году профессор Массачусетского технологического института '
                         'Джозеф Вейценбаум разработал компьютерную программу под названием Элиза. Считается, '
                         'что это первый чат-бот в истории. Элиза была простым чат-ботом на основе ключевых слов, '
                         'имитирующим человека-психиатра.',
                         parse_mode='html')
        mes2 = 'История'

    elif message.text == 'Перспективы😎':
        bot.send_message(message.chat.id,
                         'Чат-боты – одно из самых перспективных направлений развития искусственного интеллекта. Это '
                         'не удивительно. Ведь при использовании самообучающихся ботов можно получить прибыль. А это '
                         'главный двигатель развития технологии. Сегодня кроме текстовых ответов можно '
                         'взаимодействовать с чат-ботом через голос. Успехи Алисы от Яндекса и Олега от Тинькофф '
                         'подстегнули отрасль. Все больше крупных компаний развивают своих голосовых ассистентов.',
                         parse_mode='html')
        mes2 = 'Перспективы'

    elif message.text == 'Тема работы🥼':
        bot.send_message(message.chat.id, '🤖Bot-ы. История и перспективы🤖', parse_mode='html')
        mes2 = 'Тема работы'
    elif message.text == 'НЕТ😵😵':
        bot.send_message(message.chat.id, 'хехе', parse_mode='html')
        mes2 = 'хехе'
        time.sleep(1)
        for i in range(0, 20):
            sti = open("\stickers\\1.webm", 'rb')
            bot.send_sticker(message.chat.id, sti)

    elif message.text == 'Полезности🧩':
        bot.send_message(message.chat.id,
                         'https://russiansu.ru/prikazy/kak-pravilno-napisat-prikaz-ob-otchisleniya-studenta.html',
                         parse_mode='html')
        mes2 = 'Полезности'

    else:
        bot.send_message(message.chat.id,
                         'Мой создатель не слишком умный т.ч не удивительно что я не понял что ты сказал (┬┬﹏┬┬)',
                         parse_mode='html')
        mes2 = 'Написал ' + str(message.text)

    bot.send_message(admin_code, (mes1 + ' ' + mes2), parse_mode='html')
    a.append(Actions(mes1, mes2))
    print(mes1 + ' ' + mes2)


print('Started \n')
print('Имя бота: @newlaboratoryworkbot \n')
bot.polling(non_stop=True)

a = sorted(a, key=lambda actions: actions.name)
with open(r"actions.txt", mode='w', encoding='utf-8') as file:
    file.write('Все действия: \n\n')
    f = len('| ' + str(a[0].name + ' |'))
    file.write('-' * f + '\n')
    file.write('| ' + str(a[0].name + ' |\n\n'))
    for i in range(0, len(a)):
        if a[i].name != a[i - 1].name:
            f = len('| ' + a[i].name + ' |')
            file.write('-' * f + '\n')
            file.write('| ' + a[i].name + ' |')
            file.write(': \n')
        file.write(a[i].act)
        file.write('\n')
