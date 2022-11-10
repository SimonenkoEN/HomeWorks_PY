# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# а) AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E

with open ("task_024_1.txt","r") as t24_1:
    s = t24_1.readline()
print(s)

for i in range(len(s)-2,-1,-1):
    if s[i] != s[i+1]:
        s = s[:i+1]+","+s[i+1:]
l =s.split(",")
for i in range(len(l)):
    c = l[i][0]
    n = l[i].count(c)
    l[i] = str(n)+c
s2 = "".join(l)
print(s2)

with open ("task_024_2.txt","w") as t24_2:
    t24_2.write(s2)


with open ("task_024_2.txt","r") as t24_2:
    s3 = t24_2.readline()
print(s3)

a = len(s3)
i = 0
while i < a:
    try:
        n = int(s3[i])
        i += 1
    except:
        s3 = s3[:i+1]+","+s3[i+1:]
        a += 1
        i += 2
l2 = s3.split(",")
l2.pop(-1)
for i in range(len(l2)):
    c = l2[i][-1]
    l2[i] = l2[i].replace(c,'')
    n = int(l2[i])
    l2[i] = c * n
s4 = ''.join(l2)
print(s4)

with open ("task_024_1.txt","w") as t24_1:
    t24_1.write(s4)