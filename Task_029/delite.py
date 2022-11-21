import get_data as gd
from search import search_by_value as sv

def delite_line():
    data=gd.get_data("base.csv")
    value=input("Введите фамилию: ")
    value=value.upper()
    if sv(1,value,data)>0:
        id=input("Введите ID удаляемой записи: ")
        n=0
        for i in data:
            if id==i[0]:
                n=n+1
                data.remove(i)
                break
        if n==0:
            print("ID введен неверно")  
        else:
            with open ("base.csv","w") as bd:
                for line in data:
                    line=','.join(line)
                    bd.write(line)
                    bd.write("\n")
            print("Данные успешно удалены") 
    
