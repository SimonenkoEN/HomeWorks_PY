
import telebot
from telebot import types


bot=telebot.TeleBot(token)

c=""

@bot.message_handler(commands=["start"])
def start(message):
    markup=types.ReplyKeyboardMarkup (resize_keyboard=True)
    button=types.KeyboardButton(text="База данных спортивной школы")
    markup.add(button)
    bot.send_message(message.chat.id, text="Здравствуйте. Я бот для работы с базой данных спортивной школы.",reply_markup=markup)
@bot.message_handler(content_types=["text"])
def func(message):
    if (message.text=="База данных спортивной школы"):
        markup=types.ReplyKeyboardMarkup (resize_keyboard=True)
        button1=types.KeyboardButton(text="Вывести все записи")
        button2=types.KeyboardButton(text="Создание новой записи")
        button4=types.KeyboardButton(text="Поиск записи")
        button5=types.KeyboardButton(text="Удаление записи")
        button6=types.KeyboardButton(text="Вернуться в главное меню")
        markup.add(button1, button2,button4,button5,button6 )
        bot.send_message(message.chat.id, text="Выберите нужное действие",reply_markup=markup)
    elif (message.text=="Вывести все записи"): 
        with open ("base.csv","r") as bd:
            for lst in bd:
                lst=lst.replace(",","  ")
                bot.send_message(message.chat.id, text=lst)
    elif (message.text=="Создание новой записи"): 
        global c
        bot.send_message(message.from_user.id,"Введите фамилию")
        bot.register_next_step_handler(message,start_reg)
    elif (message.text=="Поиск записи"): 
        bot.send_message(message.chat.id, text="Введите элемент ФИО для поиска") 
        bot.register_next_step_handler(message,search_line)
    elif (message.text=="Удаление записи"):
        bot.send_message(message.chat.id, text="Введите ID удаляемой записи: ") 
        bot.register_next_step_handler(message,delete_line)
    elif (message.text=="Вернуться в главное меню"):
        start(message)
        bot.register_next_step_handler(message,func)
 
def start_reg(message):
    global c
    c=message.text
    bot.send_message(message.from_user.id,"Введите Имя")
    bot.register_next_step_handler(message,get_name)
def get_name(message):
    global c
    c=c +" "+message.text
    bot.send_message(message.from_user.id,"Введите Отчество")
    bot.register_next_step_handler(message,get_patrname)
def get_patrname(message):
    global c
    c=c +" "+message.text
    bot.send_message(message.from_user.id,"Введите год рождения")
    bot.register_next_step_handler(message,get_date)
def get_date(message):
    global c
    c=c +","+message.text
    bot.send_message(message.from_user.id,"Введите спортивную группу")
    bot.register_next_step_handler(message,get_sportgroop)
def get_sportgroop(message):
    global c
    c=c +","+message.text
    bot.send_message(message.from_user.id,"Введите спортивный разряд")
    bot.register_next_step_handler(message,get_sportlevel)
def get_sportlevel(message):
    global c
    c=c +","+message.text
    bot.send_message(message.from_user.id,"Введите номер телефона")
    bot.register_next_step_handler(message,get_namber)
def get_namber(message):
    global c
    id=add_new_line() 
    c=str(id)+","+c +","+message.text
    c=str.upper(c)
    id=add_new_line()         
    with open ("base.csv","a") as bd:
        bd.write(c)
        bd.write("\n")
    bot.send_message(message.chat.id, text=c)
    bot.send_message(message.chat.id, text="Запись сохранена")
    start(message)
    bot.register_next_step_handler(message,func)

def add_new_line():
    data=[]
    with open ("base.csv","r") as bd:
        for line in bd:
            data.append(line[:-1].split(","))
    if len(data):
        id=int(data[-1][0])+1
    else:
        id=1
    return id 
def search_line(message):
    value=message.text
    value=str.upper(value)
    data=[]
    with open ("base.csv","r") as bd:
        for line in bd:
            data.append(line[:-1].split(","))
    n=0   
    for lst in data:
        if value in lst[1]:
           n=n+1
           l=" ".join(lst)
           bot.send_message(message.chat.id, text=l)
    if n==0:
        bot.send_message(message.chat.id, text="\nПоиск не дал результатов")
    start(message)
    bot.register_next_step_handler(message,func)

def delete_line(message):
    id=message.text
    data=[]
    with open ("base.csv","r") as bd:
        for line in bd:
            data.append(line[:-1].split(","))   
    n=0
    for i in data:
        if id==i[0]:
            n=n+1
            data.remove(i)
            break
    if n==0:
        bot.send_message(message.chat.id, text="ID введен неверно")
    else:
        with open ("base.csv","w") as bd:
            for line in data:
                line=','.join(line)
                bd.write(line)
                bd.write("\n")
        bot.send_message(message.chat.id, text="Данные успешно удалены")
    start(message)
    bot.register_next_step_handler(message,func)    
bot.polling(none_stop=True)
   



