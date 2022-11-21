import get_data as gd

def print_to_console():   
    data=gd.get_data("base.csv")
    if len(data)==0:
        print("Данные отсутствуют")
        return 
    else:
        print("Варианты сортировки (по умолчанию по ID):")
        print("1. По ФИО")
        print("2. По году рождения")
        print("3. По спортивной группе")
        print("4. По спортивному разряду")    
        k=input("Выберите вариант сортировки: ")
        if k in ["1","2","3","4"]:
            data=sorted(data, key=lambda x: x[int(k)])
        lst=["ID", "ФИО","Год рождения", "Спорт.группа", "Разряд", "Телефон"]
        print(f"{lst[0]:4} {lst[1]:36} {lst[2]:12} {lst[3]:12} {lst[4]:6} {lst[5]:12}")
        for lst in data:
            print(f"{lst[0]:4} {lst[1]:36} {lst[2]:12} {lst[3]:12} {lst[4]:6} {lst[5]:12}")











    
