# Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой
# находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
print("Введите координаты точки по оси x")
x = int(input())
print("Введите координаты точки по оси y")
y = int(input())
if (x>0 and y>0):
    print("Точка принадлежит 1 четверти")
elif (x < 0 and y > 0):
    print("Точка принадлежит 2 четверти")
elif (x < 0 and y < 0):
    print("Точка принадлежит 3 четверти")
else:
    print("Точка принадлежит 4 четверти")
