import csv
import json

data = [
    {'Name': 'Vova', 'Age': 18, 'City': 'Sumy'},
    {'Name': 'Artem', 'Age': 20, 'City': 'Kyiv'},
    {'Name': 'Bob', 'Age': 19, 'City': 'Kharkiv'}
]

csv_file = 'data.csv'
json_file = 'data.json'

try:
    with open(csv_file, 'w', newline='') as csvfile:
        # Створення об'єкту записувача CSV
        writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Age', 'City'])
        
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print("Дані було успішно записано у файл", csv_file)

    # Зчитування даних з .csv файлу
    with open(csv_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    # Запис даних у .json файл
    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print("Дані було успішно переписано у файл", json_file)

except FileNotFoundError:
    print("Файл не знайдено.")

except Exception as e:
    print("Сталася помилка:", e)

#Batrachenko Serhii

try:
    with open(json_file, 'r') as jsonfile:
        data = json.load(jsonfile)

    with open(csv_file, 'a', newline='') as csvfile:  # Відкриваємо файл у режимі додавання
        writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Age', 'City'])

        # Додавання нових рядків
        new_data = [
            {'Name': 'Max', 'Age': 22, 'City': 'Lviv'},
            {'Name': 'Anna', 'Age': 21, 'City': 'Odessa'}
        ]
        for row in new_data:
            writer.writerow(row)

    print("Нові дані було успішно додано до файлу", csv_file)

except Exception as e:
    print("Сталася помилка під час додавання нових даних:", e)

#Leonid Raiev

try:
    # Зчитування оновлених даних з початкового .csv файлу
    with open(csv_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        updated_data = [row for row in reader]

    # Додавання нових рядків до оновлених даних
    new_data = [
        {'Name': 'Ser', 'Age': 40, 'City': 'London'},
        {'Name': 'Max', 'Age': 30, 'City': 'Paris'}
    ]
    updated_data.extend(new_data)

    # Оновлення .json файлу з новими даними
    with open(json_file, 'w') as jsonfile:
        json.dump(updated_data, jsonfile, indent=4)

    print("Оновлені дані було успішно переписано у файл", json_file)

except Exception as e:
    print("Сталася помилка під час оновлення даних у файлі .json:", e)