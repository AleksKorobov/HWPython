# В первой строке входного файла INPUT.TXT записано натуральное
#  число N (1 ≤ N ≤ 100) – число монеток. В каждой из последующих
# N строк содержится одно целое число – 1 если монетка лежит решкой вверх и 0 если вверх гербом.

#lst=list(map(int, input().split()))

lst = [1,0,1,1,0]
len = len(lst)
count_one= lst.count(1)
count_zуro= lst.count(0)
if count_one>count_zуro:
    print(f'Нужно перевернуть '+ str(count_zуro) +' монет из '+ str(len))
else:
    print(f'Нужно перевернуть ' + str(count_one) +' монет из ' + str(len))
