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
