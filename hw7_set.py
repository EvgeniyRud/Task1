# Задача 1: Дані списки:
# first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Потрібно повернути список, що складається з унікальних елементів, спільних для цих двох списків.

first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(f' Common elements - {set(first) & set(second)}')

# Задача 2: У вас є 2 списка, напишіть програму, яка виводить усі елементи першого, яких немає у другому.

new_list_2a = input('Enter elements of first list with coma:')
newest_list_2a = new_list_2a.split(',')
new_list_2b = input('Enter elements of second list with coma:')
newest_list_2b = new_list_2b.split(',')
print(f' Unique elements of first list - {set(newest_list_2a) - set(newest_list_2b)}')


# Задача 3: Написати програму, яка на вхід приймає список чисел і перевіряє, чи всі числа в цій послідовності
# є унікальними

number_3 = input(f'Enter member of list (enter "end" for stop):')
list_3 = []
while number_3 != 'end':
    number_3 = int(number_3)
    list_3.append(number_3)
    number_3 = input(f'Enter next member of list :')
set_3 = set(list_3)
if len(list_3) == len(set_3):
    print('All elements are unique')
else:
    print('List has duplicats')


# Задача 4: Написати програму, яка знайде мінімальне значення у списку.
# Список задати у самій програмі у вигляді: elements = [1, 5, 68, 0]
# У ньому може бути скільки завгодно елементів


number_4 = input(f'Enter member of list (enter "end" for stop):')
list_4 = []
while number_4 != 'end':
    number_4 = int(number_4)
    list_4.append(number_4)
    number_4 = input(f'Enter next member of list :')
min_number = list_4[0]
for i in range(1,len(list_4)):
    if list_4[i] < min_number:
        min_number = list_4[i]
print(f'Minimum number is {min_number}')


#
# Задача 5. Написати програму, яка порахує суму всіх елементів у списку
# Список задати у самій програмі у вигляді: elements  = [1, 5, 68, 0]
# У ньому може бути скільки завгодно елементів
# P.S Функції min() і sum() використовувати в останніх 2 задачах не можна. Цикли для вирішення
# можуть використовуватися які хочете( while або for)

number_5 = input(f'Enter member of list (enter "end" for stop):')
list_5 = []
sum_elements = 0
while number_5 != 'end':
    number_5 = int(number_5)
    list_5.append(number_5)
    number_5 = input(f'Enter next member of list (enter "end" for stop) :')
for element in list_5:
    sum_elements += element
print(f'Sum of elements is {sum_elements}')
