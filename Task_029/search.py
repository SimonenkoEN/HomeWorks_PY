import get_data as gd

def search_data():
    data=gd.get_data("base.csv")
    print("Выберите параметр поиска.")
    print("1. Поиск по фамилии")
    print("2. Поиск по году рождения")
    print("3. Поиск по спортивной группе")
    print("4. Поиск по спортивному разряду")
    print("5. Поиск по телефону")
    print("any key - ВЫХОД ")
    index=input("Выберите необходимый пункт меню: ")
    if index in ["1","2","3","4","5"]:
        sv=input("Введите искомые данные: ")
        sv=sv.upper()
        search_by_value(int(index),sv,data)


def search_by_value(index, search_value,data):
    n=0
    for lst in data:
        if search_value in lst[index]:
            n=n+1
            if n==1:
                l=["ID", "ФИО","Год рождения", "Спорт.группа", "Разряд", "Телефон"]
                print(f"{l[0]:4} {l[1]:36} {l[2]:12} {l[3]:12} {l[4]:6} {l[5]:12}")
            print(f"{lst[0]:4} {lst[1]:36} {lst[2]:12} {lst[3]:12} {lst[4]:6} {lst[5]:12}")
    if n==0:
        print("\nПоиск не дал результатов")
    return n
