# Даны два файла, в каждом из которых находится запись многочлена.
# (файлы можно создать в task_019.py)
# Задача - сформировать файл, содержащий сумму многочленов.

with open ('file1.txt',"r") as f1:
    s1=f1.read()
print(s1)
with open ('file2.txt',"r") as f2:
    s2=f2.read()
print(s2)

def get_split(s): # Рзделяем строку с многочленом на элементы необходимые для работы (создание списка из элементов)
    s=s.replace("=0","")
    s=s.replace("x","x1")
    s=s.replace("1^","")
    l=s.split("+")
    for i in range(len(l)):
        if l[i][0]=='x':
            l[i]='1'+l[i]
        l[i]=l[i].split("x")
    if len(l[-1])==1:
        l[-1].append(0)
    return l

l1=get_split(s1)
l2=get_split(s2)
# print(l1)
# print(l2)

for i in range(len(l1)): # В списке первого многочлена коэффициенты эдементов складываем с одностепенными коэффициентами из списка второго многочлена
    for j in range(len(l2)):
        if l2[j][1]==l1[i][1]:
            l1[i][0]=str(int(l1[i][0])+int(l2[j][0]))

for j in range(len(l2)): # Добавляем в список первого многочлена недостающие элементы из второго
    n=True
    for i in range(len(l1)):        
        if l1[i][1]==l2[j][1]:
            n=False
    if n:
        l1.append(l2[j])

for i in range(len(l1)-1): # Сортировка списка по убыванию степеей
    for j in range(i+1,len(l1)):
        if int(l1[i][1])<int(l1[j][1]):
            l1[i],l1[j]=l1[j],l1[i]

# Формирование строку с новым многочленом
s="=0"
for i in range(len(l1)-1,0,-1): 
    if int(l1[i][0])==1 and int(l1[i][1])!=0:
        l1[i][0]=''
    if int(l1[i][1])==0:
        s="+"+l1[i][0]+s
    elif int(l1[i][1])==1:
        s="+"+l1[i][0]+"x"+s
    elif int(l1[i][1])>1:
        s="+"+l1[i][0]+"x^"+l1[i][1]+s
if int(l1[0][1])>1:
    if l1[0][0]=='1':
        s="x^"+l1[0][1]+s
    else:
        s=l1[0][0]+"x^"+l1[0][1]+s
else:
    s=l1[0][0]+"x"+s
print (s)

with open('file.txt',"w") as f:
    f.write(s)