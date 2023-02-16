# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.

# a = int(input('Введите первый элемент прогрессии: '))
# b = int(input('Введите разность:  '))
# k = int(input('Введите количество элементов: '))
# res = [a]
# for _ in range(k-1):
#     a += b
#     res.append(a)

# print(res)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
from random import randint
# my_list = [randint(-5,10) for _ in range(10)]

# min_d = int(input("Введите минимальное значение диапозона: "))
# max_d = int(input("Ведите максимальное значение диапозона: "))
# res = []
# for i in range(len(my_list)):
#     if min_d <= my_list[i] <= max_d:
#         res.append(i)
# print(my_list)
# print(res)


# Задача HARD SORT необязательная.
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10

col = int(input('Задайте количество столбцов: '))
row = int(input("Задайте количество строк: "))

def create_2Darr(col, row):
    arr = [randint(1,10) for _ in range(col*row)]
    arr2D = []
    for i in range(0, len(arr), row):
        arr2D.append(arr[i:i+row])
    return arr2D

def create_2Darr_enum(col, row):
    arr = [x+1 for x in range(col*row)]
    arr2D = []
    for i in range(0,len(arr), row):
        arr2D.append(arr[i:i+row])
    return arr2D

def view_2Darr_table(lst):
    for elm in lst:
        print(*elm)

# my_arr_2D = create_2Darr(col,row)
# view_2Darr_table(my_arr_2D)

def sort_2Darr(lst2D):
    row = len(lst2D[0])
    res_arr = []
    res_arr2D = []
    for elm in lst2D:
        res_arr+=elm
    res_arr.sort()
    for i in range(0, len(res_arr), row):
        res_arr2D.append(res_arr[i:i+row])
    return res_arr2D
# print('============================')
# view_2Darr_table(sort_2Darr(my_arr_2D))

# задача 2 HARD необязательная
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , 
# причем чтоб количество элементов было четное. 
# Вывести на экран красивенько таблицей. 
# Перемешать случайным образом элементы массива, 
# причем чтобы каждый гарантированно и только один раз переместился 
# на другое место и выполнить это за m*n / 2 итераций. 
# То есть если массив три на четыре, то надо выполнить не более 6 итераций.
# И далее в конце опять вывести на экран как таблицу.

arr2D = create_2Darr_enum(col,row)

def uniq_swap(arr2D):
    row = len(arr2D[0])
    arr = []
    res_arr2D = []
    for elm in arr2D:
        arr+=elm
    fin_arr = []
    for i in range(int(len(arr)/2)):
        idx = randint(i+1,len(arr)-1)
        arr[i], arr[idx] = arr[idx], arr[i]
        fin_arr.extend([arr[idx], arr[i]])
        arr.pop(idx)
    for i in range(0, len(fin_arr), row):
        res_arr2D.append(fin_arr[i:i+row])
    return res_arr2D

view_2Darr_table(arr2D)
print("=============================")
view_2Darr_table(uniq_swap(arr2D))