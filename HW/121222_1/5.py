# Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math
print("Введите координату х первой точки:")
x1 = int(input())
print("Введите координату у первой точки:")
y1 = int(input())
print("Введите координату х второй точки:")
x2 = int(input())
print("Введите координату у второй точки:")
y2 = int(input())
d = round(math.sqrt((x1-x2)**2+(y1-y2)**2),2)
print(d)
