# Создайте программу для игры в ""Крестики-нолики"".

import os

sign_pl1, sign_pl2 = '⛌', '𐩒'
turn = pl = 0
free_cell = [str(i) for i in range(1, 10)]
field = [[' ' for i in range(3)] for i in range(3)]
game_not_over = True

def set_cell():
    while True:
        cell = input()
        if cell in free_cell:
            free_cell.remove(cell)
            return int(cell)
        else:
            print('Нет такого номера или эта клетка занята.', end=' ')

def get_cell(cell, sign):
    if cell == 1:
        field[0][0] = sign
    elif cell == 2:
        field[0][1] = sign
    elif cell == 3:
        field[0][2] = sign
    elif cell == 4:
        field[1][0] = sign
    elif cell == 5:
        field[1][1] = sign
    elif cell == 6:
        field[1][2] = sign
    elif cell == 7:
        field[2][0] = sign
    elif cell == 8:
        field[2][1] = sign
    elif cell == 9:
        field[2][2] = sign

def print_field(l):
    print('Введите номер клетки игроаого поля')
    print(l[0][0]+' |'+l[0][1]+' |'+l[0][2]+'     1  2  3')
    print('――|――|――')
    print(l[1][0]+' |'+l[1][1]+' |'+l[1][2]+'     4  5  6')
    print('――|――|――')
    print(l[2][0]+' |'+l[2][1]+' |'+l[2][2]+'     7  8  9')

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

os.system('CLS')
print_field(field)
while game_not_over:
    turn += 1
    if turn%2 == 1:
        pl = 1
        sgn = sign_pl1
    else:
        pl = 2
        sgn = sign_pl2
    print(f'Ход {pl} игрока:', end=' ')
    get_cell(set_cell(),sgn)
    os.system('CLS')
    print_field(field)
    game_not_over = is_not_game_over(field, sgn)
    if not game_not_over:
        print(f'ВЫИГРАЛ {pl} ИГРОК!')
    elif turn == 9:
        print('НИЧЬЯ')
        break