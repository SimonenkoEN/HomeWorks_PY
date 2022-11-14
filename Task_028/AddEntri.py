
def AddEntri():
    t= str.capitalize(input("Фамилия: "))+","+str.capitalize(input("Имя: "))+","+str.capitalize(input("Телефон: "))
    with open('phone_book.csv','a',encoding="UTF") as f:
        f.write(t)
        f.write("\n")
    print("Контакт сохранен")