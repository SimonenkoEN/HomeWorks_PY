import telebot
from telebot import types
import datetime
from calc import *

bot = telebot.TeleBot('5961055198:AAG3fA9n89y3_fwi1s0jDqjR1f9JbjkXpGs')

def loger(message, res):
    dt = datetime.datetime.now()
    file = open('db.csv', 'a', encoding='utf')
    file.write(f'{dt}: {message.chat.first_name} {message.chat.last_name}, user id: {message.from_user.id}, text: {message.text} = {res} \n')
    file.close()

@bot.message_handler(commands=["start"])
def start(message):
    markup=types.ReplyKeyboardMarkup (resize_keyboard=True)
    button1=types.KeyboardButton(text='Калькулятор')
    button2=types.KeyboardButton(text='Калькулятор обычных дробей')
    button3=types.KeyboardButton(text='Калькулятор комплексных чисел')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, text='Здравствуйте. Я бот-калькулятор.\nНеобходимо выбрать тип калькулятора' ,reply_markup=markup)

@bot.message_handler(content_types=['text'])
def menu(message):
    if (message.text=='Калькулятор'):
        bot.send_message(message.from_user.id,'Введите выражение вида:\n(a)арифметическое дествие(b)\nгде a и b - вещественные числа\nПример: (-0.5)+(2)')
        bot.register_next_step_handler(message,fcalc)
    elif (message.text=='Калькулятор обычных дробей'):
        bot.send_message(message.from_user.id,'Введите выражение вида:\n(a/b)арифметическое дествие(c/d)\nгде a, b, c и d - целые числа\nПример: (2/3)-(3/7)')
        bot.register_next_step_handler(message,fcalc_rational)
    elif (message.text=='Калькулятор комплексных чисел'):
        bot.send_message(message.from_user.id,'Введите выражение вида:\n(a+bi)арифметическое дествие(c+di)\nгде a, b, c и d - вещественные числа\nПример: (-3-5i)*(7+4i)')
        bot.register_next_step_handler(message,fcalc_complex)
    else:
        bot.send_message(message.from_user.id,'Ошибка ввода!')
        start(message)
        bot.register_next_step_handler(message,menu)


def fcalc(message):
    try:
        res = calc(message.text)
        loger(message, res)
    except:
        res = 'Ошибка ввода!\nВыражение введено неверно'
    bot.send_message(message.from_user.id,res)
    start(message)
    bot.register_next_step_handler(message,menu)


def fcalc_rational(message):
    try:
        res = calc_rational(message.text)
        loger(message, res)
    except:
        res = 'Ошибка ввода!\nВыражение введено неверно'
    bot.send_message(message.from_user.id,res)
    start(message)
    bot.register_next_step_handler(message,menu)

def fcalc_complex(message):
    try:
        res = calc_complex(message.text)
        loger(message, res)
    except:
        res = 'Ошибка ввода!\nВыражение введено неверно'
    bot.send_message(message.from_user.id,res)
    start(message)
    bot.register_next_step_handler(message,menu)

bot.infinity_polling()