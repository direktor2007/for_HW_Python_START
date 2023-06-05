# ; Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# ;  (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
list_1 = [random.randint(-10, 10) for i in range(n)]
n = int(input("Введите число  "))
min_number = int(input())
max_number = int(input())
for i in range(len(list_1)):
        if min_number <= list_1[i] <= max_number:
            print(i)




# from random import randint
# n = int(input('n = '))
# lst = [randint (n, n) for i in range(2 * n)]
# print(lst)
# print(min_num := randint(-n, 0), end=' ')
# print(max_num := randint(0, n))

# for i in range(2 * n):
#     if min_num <= lst[i] <= max_num:
#         print(1, end=" ")