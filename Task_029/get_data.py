def get_data(file):
    data=[]
    with open (file,"r") as bd:
        for line in bd:
            data.append(line[:-1].split(","))
    return data


def check_double_line(data,name):
    n=0
    for i in data:
        if i[1]==name:
            n+=1
            if n==1:
                print("Найдены совпадения:")
            print( " ".join(i))
    return n
