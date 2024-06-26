text = """У місті, де кожен крок – це нова історія,
          життя пульсує ритмом міста, сповненого сюрпризів і 
          незабутніх моментів. Вулиці вкриті кольоровими ліхтарями, 
          які вночі розкривають свою магію. В парках грає музика джазу,
          заворожуючи слухачів своєю мелодією. Люди з різних куточків світу 
          зустрічаються тут, діляться своїми історіями й ідеями. Кожен день – 
          це нові враження, нові знайомства, нові перспективи. Місто живе своїм життям,
          а в кожному його кутку таємниця і пригода, що чекає на свого відкривача."""

#Berdenko Volodymyr
# Визначення довжини рядка
length = len(text)
print("Довжина рядка:", length)

# Розбиття рядка на слова
words = text.split()
print("Слова у тексті:", words)

# Об'єднання списку слів у рядок з роздільником " "
new_text = " ".join(words)
print("Новий текст:", new_text)

#Batrachenko Serhii
word = text.upper()
print("new text", word)

new_Text = text.replace("нова історія", "new history")
print(new_Text)

print(text.strip(','))

#Fomin Vladyslav
if text.startswith(("У місті")):
    print("Строка начинается с 'У місті' '")
else:
    print("Строка не начинается ни с 'У місті', ни с 'ПИПИПУ'")

index = text.find("ритмом міста")
if index != -1:
    print(f"Підстрока 'ритмом міста' знайдена в позиції {index}")
else:
    print("Підстрока 'ритмом міста' не знайдена")


count = text.count("історія")
print(f"Кількість входів 'історія' в строці: {count}")

#Leonid Raiev

capitalized_text = text.capitalize()
print("Текст з великої літери:", capitalized_text)

is_digit = text.isdigit()
print("Текст складається тільки з цифр:", is_digit)

split_lines = text.splitlines()
print("Текст, розбитий на рядки:", split_lines)