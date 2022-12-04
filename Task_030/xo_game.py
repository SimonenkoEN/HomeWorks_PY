import telebot

def set_cell(cell, lst, sign):
    if cell == '1':
        lst[0][0] = sign
    elif cell == '2':
        lst[0][1] = sign
    elif cell == '3':
        lst[0][2] = sign
    elif cell == '4':
        lst[1][0] = sign
    elif cell == '5':
        lst[1][1] = sign
    elif cell == '6':
        lst[1][2] = sign
    elif cell == '7':
        lst[2][0] = sign
    elif cell == '8':
        lst[2][1] = sign
    elif cell == '9':
        lst[2][2] = sign
    return lst

def print_field(l,turn,pl):
    fil = l[0][0]+' |'+l[0][1]+' |'+l[0][2]+'  <- 1 2 3\n'
    fil += l[1][0]+' |'+l[1][1]+' |'+l[1][2]+'  <- 4 5 6\n'
    fil += l[2][0]+' |'+l[2][1]+' |'+l[2][2]+'  <- 7 8 9\n'
    fil += 'Ход №'+str(turn)+', ход '+str(pl)+' игрока\n '
    fil += 'Введите номер клетки игрового поля:'
    return fil

def is_not_game_over(l, sign):
    if l[0][0] == sign and l[0][1] == sign and l[0][2] == sign:
        return False
    elif l[1][0] == sign and l[1][1] == sign and l[1][2] == sign:
        return False
    elif l[2][0] == sign and l[2][1] == sign and l[2][2] == sign:
        return False
    elif l[0][0] == sign and l[1][0] == sign and l[2][0] == sign:
        return False
    elif l[0][1] == sign and l[1][1] == sign and l[2][1] == sign:
        return False
    elif l[0][2] == sign and l[1][2] == sign and l[2][2] == sign:
        return False
    elif l[0][0] == sign and l[1][1] == sign and l[2][2] == sign:
        return False
    elif l[0][2] == sign and l[1][1] == sign and l[2][0] == sign:
        return False
    else:
        return True

# def xo_game(update: Update, context: CallbackContext):
#     free_cell = [str(i) for i in range(1, 10)]
#     field = [['*' for i in range(3)] for i in range(3)]
#     turn = 0
#     update.message.reply_text(f'{print_field(field)}')
#     while True:
#         turn += 1
#         if turn%2 == 1:
#             pl = 1
#             sgn = 'X'
#         else:
#             pl = 2
#             sgn = 'O'
#         update.message.reply_text(f'Ход {pl} игрока: ')
#         while True:
#             cell = update.message.text
#             if cell in free_cell:
#                 free_cell.remove(cell)
#                 break
#         else:
#             update.message.reply_text(f'Нет такой клетки или эта клетка занята.')
#         set_cell(cell, field, sgn)
#         update.message.reply_text(f'{print_field(field)}')
#         if not is_not_game_over(field, sgn):
#             update.message.reply_text(f'ВЫИГРАЛ {pl} ИГРОК!')
#             break
#         elif turn == 9:
#             update.message.reply_text(f'НИЧЬЯ')
#             break
