import get_data as gd
from search import search_by_value as sv

def edit_line():    
    data=gd.get_data("base.csv")
    value=input("Введите фамилию: ")
    value=value.upper()
    if sv(1,value,data)>0:
        id=input("Введите ID редактируемой записи: ")
        n=0
        for i in data:
            if id==i[0]:
                n=n+1
                for k in range(1,6):
                    print(f"Текущие данные: {i[k]}")
                    new_data=input("Для записи введите новые данные, иначе нажмине ENTER: ")
                    if new_data!="":
                        i[k]=new_data.upper()
                print(" ".join(i))                
                break
        if n==0:
            print("ID введен неверно")  
        else:
            with open ("base.csv","w") as bd:
                for line in data:
                    line=','.join(line)
                    bd.write(line)
                    bd.write("\n")
            print("Данные успешно изменены")
         
    