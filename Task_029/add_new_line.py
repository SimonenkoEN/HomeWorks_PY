import get_data as gd

def add_new_line():
    data=gd.get_data("base.csv")
    if len(data):
        id=int(data[-1][0])+1
    else:
        id=1
    name=input("Фамилия: ")+" "
    name+=input("Имя: ")+" "
    name+=input("Отчество: ")   
    if gd.check_double_line(data,name)>0:
        mode=input("Если вы хотите продолжить ввод данных нажмите пробел. Если нет - любую другу клавишу: ")
        if mode!=" ":
            return
    dr=input("Год рождения: ")
    sport_group=input("Спортивная группа: ")
    sport_level=input("Спортивный разряд: ")
    phone=input("Номер телефона: ")
    line=name+","+dr+","+sport_group+","+sport_level+","+phone
    line=line.upper()
    print(line.replace(","," "))
    print("Действия:")
    print("1. Сохранить запись")
    print("2. Ввести заново")
    print("any kay - Выйти из режима 'Добавление записи' без сохранения")
    value=input("Выбрать вариант действий")
    if value=="1":
        line=str(id)+","+line
        with open ("base.csv","a") as bd:
            bd.write(line)
            bd.write("\n")
        print("Данные успешно сохранены.")
    elif value=="2":
        add_new_line()
    
