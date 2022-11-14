import os
import search_module as sm
import print_to_console as pc
import AddEntri as Add

def main_screen():
    os.system('CLS')
    print('ТЕЛЕФОННЫЙ СПРАВОЧНИК')
    print('***********************')

def start_button():
    main_screen()
    print('Выберите режим работы со справочником')
    mode = input('1 - поиск по Фамилии, 2 - поиск по номеру телефона, 3 - добавление контакта, any key - выход: ')
    main_screen()
    if mode=="1":
        last_name=input('Введите фамилию: ')
        result=sm.search_method_1(last_name)
    elif mode=="2":
        last_name=input('Введите номер телефона: ')
        result=sm.search_method_2(last_name)
    elif mode=="3":
        Add.AddEntri()
        return
    else:         
        return
    if len(result)==0:
        print("Поиск не дал результата.")
        mode2=input("1-повторить поиск, 2-добавить новый контакт, eny key - выход: ")
        if mode2=="1":
            start_button()
        elif mode2=="2":
            Add.AddEntri()
        else:
            return
    pc.Print_Result(result)


