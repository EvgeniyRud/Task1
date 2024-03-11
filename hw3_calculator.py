print('Введіть перше число ')
number_1 = int(input())
print('Введіть дію (можливі дії: +,-,/,* ) ')
action = input()
if action == "+" or action == "-" or action == "/" or action == "*":
    print('Введіть друге число ')
    number_2 = int(input())
    if action == "+":
        print(number_1+number_2)
    elif action == "-":
        print(number_1 - number_2)
    elif action == "*":
        print(number_1 * number_2)
    elif action == "/":
        print(number_1 / number_2)
else:
    print("Недопустима дія")



