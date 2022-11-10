# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

bin = [0, 1]
count = 0
print('x y z ¬(x ⋁ y ⋁ z) ¬x ⋀ ¬y ⋀ ¬z')
for x in bin:
    for y in bin:
        for z in bin:
            if not(x or y or z) == ((not x) and (not y) and (not z)):
                count += 1
            print(f'{x} {y} {z} {not(x or y or z):^12} {(not x) and (not y) and (not z):^12}')
if count == 2 ** 3:
    print('The statement is true')
else:
    print('The statement is false')