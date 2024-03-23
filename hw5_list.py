# 1. Написати програму, яка перевіряє чи є стрінга паліндромом

text_message = input('Enter text please :')
text_compare = text_message.lower() # На випадок першої заглавної літери роблю всі букви маленькими
print(f' Is {text_message} palindrome? - {text_compare == text_compare[::-1]} ')

# 2. Ви маєте список ['Hillel', 'AQA', 'TEST'], переведіть цей список в стрінгу, а потім знову в список
new_list = ['Hillel', 'AQA', 'TEST']
new_string = ' '.join(new_list)
newest_list = new_string.split()
print (new_string, type(new_string),'\n',newest_list, type(newest_list))

# 3. Ви маєте список ['Tst', 'aBc', 'TEST', 'Hello', "neW'],
# відсортуйте його, але врахуйте що слова в списку можуть  починатися з великої або малої літери
new_list_1 = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']
new_list_1.sort(key = str.lower)
print(new_list_1)

# 4. Ви маєте список [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]],
# дістаньте з нього значення 'Win' та переведіть його у новий список. Результат має бути  ['Win']
new_list_2 = [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]]
newest_list_2 = new_list_2[-1][-1]
print(newest_list_2)

# 5. Створіть будь який список та перевірте чи коректно він відсортований
new_list_3 = input('Enter elements of list with coma:')
newest_list_3 = new_list_3.split(',')
newest_list_3sort = newest_list_3.copy()
newest_list_3sort.sort(key = str.lower)
print(f'Is list {newest_list_3} sorted correctly? - {newest_list_3==newest_list_3sort}')




