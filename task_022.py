# Создайте программу для игры с конфетами человек против 
# человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два 
# игрока делая ход друг после друга. Первый ход определяется
#  жеребьёвкой. За один ход можно забрать не более чем 28
#  конфет. Все конфеты оппонента достаются сделавшему 
# последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Победная стратегия: Изначальное число(N) конфет делим на максимальное количество конфет(x), которое можно взять. 
# Первому игроку, который собирается выиграть, необходимо первым ходом взять 20 конфет((2021-20)%29==0). 
# Далее нам это будет необходимо для дальнейшей стратегии.
# В последующие ходы необходимо добирать количество конфет взятые противником до 29, что в конечном итоге приведет к победе первого игрока.
# Поэтому победить первого игрока, который знает стратегию практически невозможно. 
# Однако если первый игрок выбрал любое другое количество конфет. То победная стратегия прописанная в боте не позволит первому игроку выиграть.
#Для возможности игроку, не знающему победную стратегию, выиграть, в функцию бота была введена рандомная вероятность его ошибки.

import os
from random import randint

def grand_choise():
    try:
        type_lst = [1,2]
        num=int(input("Укажите нужный вариант (1 млм 2): "))
        if not num in type_lst:
            print("Попробуйте еще раз.")
            return grand_choise()
        else:
            return num      
    except:
        print("Попробуйте еще раз.")
        return grand_choise()


def get_candyes ():
    try:
        num=int(input("Введите число конфет от 1 до 28, которые хотите взять: "))
        if not (1<=num<=28):
            print("Попробуйте еще раз.")
            return get_candyes() 
        else:
            return num      
    except:
        print("Попробуйте еще раз.")
        return get_candyes()

def Killer_Bot(candyes, level):
    if candyes<=28:
        return candyes
    else:
        y=candyes%29
        x=randint(1,10) 
    # Рандомное значение х позволяет игроку, играющему против бота, иметь больше шансов для выигрыша. 
    # Если этого условия не будет, то стратегия без значения х даст боту возможность в игре
    # с игроком не знающим выигрышную стратегию выиграть с почти 100% вероятностью. 
        if not y==0 and (1<=x<=level):
            return y
        else:
            return randint(1,28)

os.system("CLS")
print('1. player vs player\n2. player vs bot')
game_type = grand_choise()
if game_type == 2:
    os.system("CLS")
    print('1. easy level\n2. hard level')
    game_level = grand_choise()

os.system("CLS")
if game_type == 1:
    name1 = input("Введите имя первого игрока: ")
    name2 = input("Введите имя второго игрока: ")
    # жеребьевка
    r=randint(1,101) % 2
    if r==0:
        player1_name = name1
        player2_name = name2
    else:    
        player1_name = name2
        player2_name = name1
else:
    name1 = input("Введите ваше имя: ")
    player1_name = name1

all_candyes = 117
turn = 0
while all_candyes > 0:
    os.system("CLS")
    turn+=1
    if turn % 2 != 0:
        if game_type == 2 and turn != 1:
            print(f'Бот взял конфет: {player2}')
        print(f"Конфет на столе:{all_candyes}\n{player1_name}, ваш ход!")
        player1 = get_candyes()
        all_candyes -= player1
    else:        
        if game_type == 1: #  player vs player
            print(f"Конфет на столе:{all_candyes}\n{player2_name}, ваш ход!")
            player2 = get_candyes()
        else: # player vs bot
            if game_level == 1: # easy level
                player2 = Killer_Bot(all_candyes, 2)
            else: # hard level
                player2 = Killer_Bot(all_candyes, 8)
        all_candyes -= player2
os.system("CLS")
if game_type == 1:
    if turn%2!=0:
        print(f"Поздравляю, {player1_name}, вы победили!")
    else:
        print(f"Поздравляю, {player2_name}, вы победили!")
    print("ВНИМАНИЕ!!! Черезмерное употребление сладкого может привести к диабету!")
else:
    if turn%2!=0:
        print(f"Поздравляю, {player1_name}, вы победили!")
        print("ВНИМАНИЕ!!! Черезмерное употребление сладкого может привести к диабету!")
    else:
        print(f"К сожадению, {player1_name}, вы проиграли!")    