# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# print("Введите значение x:")
# x = int(input())
# print("Введите значение у:")
# y = int(input())
# print("Введите значение z:")
# z = int(input())
# print(not (x or y or z) == (not x and not y and not z))

for x in range(2):
    for y in range(2):
        for z in range(2):
            print((not (x or y or z) == (not (x) and not (y) and not (z))))
