# Задача 1.Напишіть програму, яка виведе всі числа зі списку, які поділяються на задане число
# Число задавати з клавіатури

numbers = int(input('Enter numbers in list :'))  # Вводимо кількість цифр у списку
number_divide = int(input('Enter number for dividing :'))  # Вводимо число, на яке будемо ділити
list_1 = []  # Створюємо список та заповнюємо його
list_final = []  # Список чисел, що поділятимуться на number_divide
for i in range(1, numbers + 1):
    member = int(input(f'Enter {i} -st,nd,rd,th  member of list :'))
    list_1.append(member)
    # Варіант 1
    if member % number_divide == 0:
        list_final.append(member)
print(list_final)

# # Варіант 2
# for i in range(numbers):
#     if list_1[i] % number_divide == 0:
#         print(list_1[i])

# У даній задачі показав числа списку, які діляться на задане число СПИСКОМ. Можна їх виводити поодинці окремо
# Але тоді потрібно АБО щоб список був дан, а не вводився вручну, АБО робити ще один цикл (закоментив варіант2)


# Задача 2.Написати програму, яка знайде перше непослідовне число у списку# Список задати у самій програмі у
# вигляді: list = [1, 5, 68, 0]
# У ньому може бути скільки завгодно елементів
# Наприклад, дано список [1,2,3,4,6,7,8]
# Відповіддю буде число 6. Якщо список послідовний, вивести відповідне повідомлення

numbers_1 = int(input('Enter numbers in list :'))  # Вводимо кількість цифр у списку
list_2 = []  # Створюємо список та заповнюємо його
numbers_consistent = 0
for i in range(1, numbers_1 + 1):
    member = int(input(f'Enter {i} -st,nd,rd,th  member of list :'))
    list_2.append(member)
for i in range(numbers_1):
    if i != 0 and numbers_1>1 and list_2[i] - list_2[i - 1] != 1:
        print(list_2[i])
        break
    else:
        numbers_consistent += 1
if numbers_consistent == numbers_1:
    print('list is consistent')

# Задача 3.Написати цикл, який виведе  матрицю трикутника 1-5

numbers_3 = int(input('Enter size of matrix:'))  # Вводимо кількість цифр у списку
for matrix in range(1, numbers_3 + 1):
    for matrix_line in range(1, matrix + 1):
        print(matrix_line, end=' ')
    print()
