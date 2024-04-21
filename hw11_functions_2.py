def conversion_temperature(number_1, measure_1):
    if measure_1 == 'C':
        result = (f' {round(number_1 * 1.8 + 32, 1)} F')
    elif measure_1 == 'F':
        result = (f' {round(number_1 * 5 / 9 - 32, 1)} C')
    return result


try:
    number_1 = int(input('Enter temperature :'))
    measure_1 = input('Enter action (you can use: C or F ) ')
    result = conversion_temperature(number_1, measure_1)
except ValueError:
    result = 'Value Error: enter value of the temperature'
except UnboundLocalError:
    result = (f'Wrong type of temperature')

print(result)