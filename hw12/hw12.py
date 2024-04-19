# Завдання 1: Create a class describing any company. For example, Toshiba or Apple

from datetime import date

now_day_ = date.today()


class Apple:
    def __init__(self, year_found, city_hq, country_hq):
        self.year_found = year_found
        self.city_hq = city_hq
        self.country_hq = country_hq

    def history_company(self):
        print(self)
        return f' Company has worked {now_day_.year - self.year_found} years'


apple = Apple(1986, "Palo-Alto", "USA")
print(apple.history_company())


# Завдання 2: по *args в функціях (для задач нижче класи не потрібні)
# We have builtins function min(), max() but you can't use it
# Implement your own implementation of function max
# Implement your own min function

def minimum_of_list(*args):
    res_minimum = args[0][0]
    for i in range(len(args[0])):
        if args[0][i] < res_minimum:
            res_minimum = args[0][i]
    return res_minimum

def maximum_of_list(*args):
    res_maximum = args[0][0]
    for i in range(len(args[0])):
        if args[0][i] > res_maximum:
            res_maximum = args[0][i]
    return res_maximum

list_1 = input('Enter elements of list with coma:')
new_list_1 = list_1.split(',')
result_minimum = minimum_of_list(new_list_1)
result_maximum = maximum_of_list(new_list_1)
print(f' Minimum number is {result_minimum}. Maximum number is {result_maximum}')


