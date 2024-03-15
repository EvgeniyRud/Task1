number_1 = int(input('Enter number 1:'))
action = input('Enter action (you can use: +,-,/,* ) ')
if action == "+" or action == "-" or action == "/" or action == "*":
    number_2 = int(input('Enter number 1: '))
    if number_2 ==0:
        print('Division by zero')
    elif action == "+":
        print(number_1+number_2)
    elif action == "-":
        print(number_1 - number_2)
    elif action == "*":
        print(number_1 * number_2)
    elif action == "/":
        print(number_1 / number_2)
else:
    print("Incorrect action")



