# Задача 1 - Написати програму, в якій необхідно видалити всі вказані літери з стрінги(string)
line_1 = input("Enter text: ")
letter_need_to_delete = input("Enter letter: ")
final_text_1 = line_1.replace(letter_need_to_delete,"")
print(f'Result is {final_text_1}')

# Написати програму, яка візьме string і в кожному слові замінить першу літеру на велику.

line_2 = input("Enter text: ")
final_text_2 = str.title(line_2)
print(f' Final text is {final_text_2}')

#Напишіть програму яка перевертає стрінгу

line_3 = input('Enter text for changing: ')
final_text_3 = line_3[::-1]
print(f'Changing text is {final_text_3}')

# Напишіть програму яка приймає на вхід 2 стрінги та порівнює їх

line_4 = input('Enter text: ')
line_4_compare = input('Enter text for compare :')
if line_4 == line_4_compare:
    print("Texts are equals")
else:
    print("Texts are not equals")

# Напишіть програму яка візьме стрінг та повторить її задану кількість раз.

line_5 = input('Enter text: ')
koef_5 = int(input('Enter count repeats'))
print(f'Final text is : {line_5*koef_5}')

# Написати програму для підрахунку конвертації валюти

sum_6 = float(input('Enter amount :'))
currency_1 = input('Enter currency (UAH/USD/EUR) :')
if currency_1 != 'UAH' and currency_1 != 'USD' and currency_1 != 'EUR':
    print("Currency is incorrect")
else:
    print("Введіть валюту конвертації (UAH/USD/EUR)")
    currency_2 = input()
    if currency_2 != "UAH" and currency_2 != "USD" and currency_2 != "EUR":
        print("Currency is incorrect")
    else:
        if currency_1 == 'UAH':
            koef_1 = 1
        elif currency_1 == "USD":
            koef_1 = 38
        else:
            koef_1 = 40
        if currency_2 == 'UAH':
            koef_2 = 1
        elif currency_2 == "USD":
            koef_2 = 38
        else:
            koef_2 = 40
        sum_final = round(sum_6*koef_1/koef_2,2)
        print(f'Final sum is : {sum_final} {currency_2}')