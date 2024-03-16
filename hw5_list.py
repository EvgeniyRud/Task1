# Написати програму, яка перевіряє чи є стрінга паліндромом

text_message = input('Enter text please :')
text_compare = text_message.lower() # На випадок першої заглавної літери роблю всі букви маленькими
text_opposite = text_compare[::-1]
print(f' Is {text_message} palindrome? - {text_compare == text_opposite} ')

