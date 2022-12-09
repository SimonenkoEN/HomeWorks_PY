import telebot
from xo_game import *

bot = telebot.TeleBot('')

turn = 1
free_cell = [str(i) for i in range(1, 10)]
field = [['*' for i in range(3)] for i in range(3)]

@bot.message_handler(commands=['xo'])
def xo_game(message):
    global turn
    turn = 1
    global free_cell
    free_cell = [str(i) for i in range(1, 10)]
    global field
    field = [['*' for i in range(3)] for i in range(3)]
    bot.send_message(message.from_user.id, f'{print_field(field,turn,1)}')

@bot.message_handler(content_types=['text'])
def start(message):    
    global turn
    if turn%2 == 1:
        pl = 1
        sgn = 'X'
    else:
        pl = 2
        sgn = 'O'
    # bot.send_message(message.from_user.id,f'Ход №{turn}, ход  {pl} игрока: ')
    cell = message.text
    if cell in free_cell:
        free_cell.remove(cell)        
    else:
        bot.send_message(message.from_user.id,f'Нет такой клетки или эта клетка занята.')        
        return
    set_cell(cell, field, sgn)
    turn += 1
    bot.send_message(message.from_user.id,f'{print_field(field,turn,pl)}')
    if not is_not_game_over(field, sgn):
        bot.send_message(message.from_user.id,f'ВЫИГРАЛ {pl} ИГРОК!')
        return
    elif turn == 9:
        bot.send_message(message.from_user.id,f'НИЧЬЯ')
        return

bot.infinity_polling()
