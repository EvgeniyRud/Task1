# 1.Перепишіть наш калькулятор (який ми робили  в іншій домашці) за допомогою функцій.
#

number_1 = int(input('Enter first number :'))
action = input('Enter action (you can use: +,-,/,* ) ')
number_2 = int(input('Enter second number : '))

def add_number(number_1, number_2):
    print(number_1 + number_2)

def substract_number(number_1, number_2):
    print(number_1 - number_2)

def multiply_number(number_1, number_2):
    print(number_1 * number_2)

def divide_number(number_1, number_2):
    if number_2 == 0:
        print('Division by zero')
    else:
        print(number_1 / number_2)

if action == "+" or action == "-" or action == "/" or action == "*":
    if action == "+":
        add_number(number_1, number_2)
    elif action == "-":
        substract_number(number_1, number_2)
    elif action == "*":
        multiply_number(number_1, number_2)
    elif action == "/":
        divide_number(number_1, number_2)
else:
    print("Incorrect action")

# 2. Напишіть функцію is_prime, яка приймає 1 аргумент - число від 2 до 1000, і повертає
# True, якщо це просте число, і False в іншому випадку.

number_3 = int(input('Enter number :'))

def prime_number(number_3):
    count_dividers = 0
    for i in range(2, number_3):
        if count_dividers > 0:
            return False
            break
        else:
            if number_3 % i == 0:
                count_dividers += 1
    return True


result = prime_number(number_3)
print(result)
