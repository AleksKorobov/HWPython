# Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой
#   четверти (x и y).
print("Введите номер четверти на оси координат  X  и Y: ")
a = int(input())
if a==1:
    print("х принадлежит (0;+бесконечности), y принадлежит (0;+бесконечности)")
elif a==2:
    print("х принадлежит (-бесконечности; 0), y принадлежит (0;+бесконечности)")
elif a==3:
    print("х принадлежит (-бесконечности; 0), y принадлежит 1(-бесконечности; 0)")
elif a==4:
    print("х принадлежит (0;+бесконечности), y принадлежит (-бесконечности; 0)")
else:
    print("Такой четверти не существует на этой оси координат")