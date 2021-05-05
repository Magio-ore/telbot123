import telebot
from telebot import types
import config
import random
import COVID19Py
import pyowm
import requests
from bs4 import BeautifulSoup as BS


bot = telebot.TeleBot(config.TOKEN)
response = requests.get(config.url).json()




@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn12 = types.KeyboardButton('Привіт')
    markup.add(itembtn12)

    bot.send_message(message.chat.id,"Привіт, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот зроблений бути твоїм підопитним кроликом.".format(message.from_user, bot.get_me()), parse_mode='html',reply_markup=markup)

def welcome2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Ігри")
    item2 = types.KeyboardButton("😊 Як справи?")
    item3 = types.KeyboardButton("🙃 Давай поспілкуємось")
    item4 = types.KeyboardButton("💢 Інше")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Вибери щось)", reply_markup=markup)

def igri(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомне число")
    item2 = types.KeyboardButton("🀄️ Орел чи решка?")
    item3 = types.KeyboardButton("⬅️ Назад")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Ну давай зіграєм", reply_markup=markup)

def other(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item4 = types.KeyboardButton("☀️ Погода Львів")
    item5 = types.KeyboardButton("📊 Курси валют")
    item6 = types.KeyboardButton("⬅️ Назад")
    markup.add(item4, item5, item6)

    bot.send_message(message.chat.id, "Хммммм...", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомне число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == 'Привіт':
            welcome2(message)
        elif message.text == '🎲 Ігри':
            igri(message)
        elif message.text == '💢 Інше':
            other(message)
        elif message.text == '🀄️ Орел чи решка?':
            orel(message)
        elif message.text == '☀️ Погода Львів':
            weather(message)
        elif(message.text == '📊 Курси валют'):
            coins(message)
        elif (message.text == '🧧 Телеграм чат'):
            bot.send_message(message.chat.id, 'Наш телеграм чат: https://t.me/DarzoChannel')
        elif (message.text == '🎴 Діскорд канал'):
            bot.send_message(message.chat.id, 'Наш діскорд канал: https://discord.gg/R7ZutrBwkb')
        elif (message.text == '⬅️ Назад'):
            welcome2(message)
        elif message.text == '🙃 Давай поспілкуємось':
            telegramch(message)
        elif message.text == '😊 Як справи?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Добре", callback_data='good')
            item2 = types.InlineKeyboardButton("Не дуже", callback_data='bad')
            item3 = types.InlineKeyboardButton("Незнаю", callback_data='sogood')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Добре, як сам(a)?', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Я не знаю що відповісти 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот і добре 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Буває 😢')
            elif call.data == 'sogood':
                bot.send_message(call.message.chat.id, 'Що сталось? 😢')


    except Exception as e:
        print(repr(e))


def weather(message):
    r = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BB%D1%8C%D0%B2%D1%96%D0%B2')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        itermen1 = types.KeyboardButton('⬅️ Назад')
        markup.add(itermen1)

        bot.send_message(message.chat.id,"Привіт погода сьогодні у м.Львові:\n" +
        t_min + ', ' + t_max + '\n' + text, reply_markup=markup)

def orel(message):
    list = ['Орел', 'Решка']
    bot.send_message(message.chat.id,random.choice(list))


def telegramch(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🧧 Телеграм чат")
    item2 = types.KeyboardButton("🎴 Діскорд канал")
    item3 = types.KeyboardButton('⬅️ Назад')
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Ну давай, виберай куда тобі зручніше 😅", reply_markup=markup)

def coins(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('USD')
    itembtn2 = types.KeyboardButton('EUR')
    itembtn3 = types.KeyboardButton('RUR')
    itembtn4 = types.KeyboardButton('BTC')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

    msg = bot.send_message(message.chat.id,
                    "Дізнатись курс ПриватБанка (в відділеннях)", reply_markup=markup)
    bot.register_next_step_handler(msg, process_coin_step)

def process_coin_step(message):
    try:
       # убрать клавиатуру
       markup = types.ReplyKeyboardMarkup(resize_keyboard= True )
       itembtn1 = types.KeyboardButton('⬅️ Назад')
       markup.add(itembtn1)

       for coin in response:
           if (message.text == coin['ccy']):
              bot.send_message(message.chat.id, printCoin(coin['buy'], coin['sale']),
                               reply_markup=markup, parse_mode="Markdown")

    except Exception as e:
       bot.reply_to(message, 'ooops!')

def printCoin(buy, sale):
    '''Вывод курса пользователю'''
    return "💰 *Курс купівлі:* " + str(buy) + "\n💰 *Курс продажі:* " + str(sale)


if __name__ == '__main__':
    bot.polling(none_stop=True)
