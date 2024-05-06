#Berdenko Volodymyr
# Ваше прізвище
surname = "Берденко"

# Питання з програмування
question = "На що вказує параметр w при відкритті файлу?"

file_name = "questions.txt"

try:
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("Прізвище: {}\n".format(surname))
        file.write("Питання: {}\n".format(question))
    print("Дані було успішно записано у файл.")
except Exception as e:
    print("Сталася помилка під час запису даних у файл:", e)

#Batrachenko Serhii
# Ваше прізвище
new_surname = "Батраченко"
answer = "Параметр 'w' при відкритті файлу вказує на те, що файл відкривається для запису. Якщо файл вже існує, вміст файлу буде замінений новим. Якщо файл не існує, він буде створений."

# Запитання для наступного студента
next_question = "Які існують режими відкриття файлу у Python?"

try:
    with open(file_name, 'a', encoding='utf-8') as file:  # Відкриваємо файл у режимі додавання
        file.write("Прізвище: {}\n".format(new_surname))
        file.write("Відповідь: {}\n".format(answer))
        file.write("\n")  # Додаємо порожній рядок між записами
        file.write("Наступне питання: {}\n".format(next_question))
        file.write("\n")  # Додаємо порожній рядок після останнього запису
    print("Дані було успішно додано до файлу.")
except Exception as e:
    print("Сталася помилка під час запису даних у файл:", e)

