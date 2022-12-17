# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
#   и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]




lst= [2, 3, 4, 5, 6]
import math
i=0
while i<math.ceil(len(lst)/2):
    print(lst[i]*lst[len(lst)-1-i])
    i=i+1
# lst1= reverse(lst)
# i=0
# if i<(len(lst)/2)
# print(str[i-1::]*str[::-1])
# #     print("ДА")
# else:
#     print("НЕТ")
#print(math.ceil(len(lst)/2))
#print(lst[len(lst)-1-i])
