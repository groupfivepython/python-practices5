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
