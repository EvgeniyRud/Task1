# Задача 1: Є система, де є списки користувачів.
# roles = { 'admin' : [...], 'maintainer' : [...], 'manager' : [...], 'developer': [...]}
# - в цих списках треба понаписувати імена користувачів.
# При введенні імені необхідно перевірити, до якої ролі належить ця людина та вивести повідомлення виду:\
#     "Hello, <role>"
# Якщо імені немає у списках, вивести: "Hello, Guest"

roles = {'admin': [...], 'maintainer': [...], 'manager': [...], 'developer': [...]}
for key, value in roles.items():
    roles[key] = input(f'Enter name {key}:')
request_name = input('Enter request name:')
if not (request_name in roles.values()):
    print(f'Hello, Guest')
else:
    for key, value in roles.items():
        if value == request_name:
            print(f'Hello, {key} ')
            break

# Задача 2:
# Є словник :
# params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
# Є стрінга:
# initial_str = 'https://www.youtube.com/watch?'
# Треба написати програму , яка додасть до стінги всі елементи словника, результат має бути такий:
# result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'

params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'
result_link = initial_str
for key, value in params.items():
    result_link = result_link + key + '=' + value + '&'
result_link = result_link[:-1]
print(f'result_link = {result_link}')


# Задача 3: Взяти Ваш результат:
# result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
# Та вивести скільки разів кожен елемент повторюється в стрінг (результатом роботи скріпта має бути словник ,
# де ключ - це елемент стрінги, а значення - кількість повторень)
# Напиклад: {'h': 2, 't': 7, 'p': 1} ........
result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
my_dict = {}
for letters in result_link:
    my_dict[letters] = result_link.count(letters)
print(my_dict)
