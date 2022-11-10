# Напишите программу, удаляющую из текста все слова, содержащие "абв".

s = 'абвноль один дваабв три четабвыре пять'
print(s)
lst = s.split(' ')
for i in lst:
    if 'абв' in i:
        print(i)
        lst.remove(i)
print(' '.join(lst))