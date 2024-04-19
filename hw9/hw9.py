# 1. Вам потрібно створити текстовий файл(.txt) з текстом і написати програму, яка зкопіює дані
# з вашого файлу в інший текстовий файл

with open('hw9_file.txt','r',encoding='utf-8') as file:  # Чтение исходного файла
    with open('hw9_file_new.txt','w') as file_new:       # Создание под запись нового файла
        for line in file:                                # Цикл для перезаписи из одного файла в другой
            file_new.write(line)

# 2. Взяти csv файл, який додано до домашки і скопіювати тільки колонку email в інший csv файл

import csv

with open('names.csv', 'r') as file_2:
    csv_reader = csv.DictReader(file_2)

    with open('names_copy_2.csv', 'w') as file_2_new:
        fieldnames = ['email']
        csv_writer_2 = csv.DictWriter(file_2_new,fieldnames = fieldnames)

        csv_writer_2.writeheader()

        for line in csv_reader:
            for key in list(line.keys()):
                if key not in fieldnames:
                    del line[key]
            csv_writer_2.writerow(line)

# 3. У вас є словник
# course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}
# Юзер вводить з консолі ключ, за яким треба отримати значення.
# Написати програму, яка імплементує дану задачу з використанням блоку try/except
# (Треба обробити помилку якщо ключа не існує).

course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}
key_3 = input(f'Enter key:')

try:
    result = course[key_3]
except KeyError:
    result = 'Key error: enter existing key'
print(result)

