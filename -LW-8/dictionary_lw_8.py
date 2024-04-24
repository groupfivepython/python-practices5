#Berdenko Volodymyr

# Створення порожнього словника для зберігання даних про студентів
students_dict = {}

# Функція для додавання даних про студента до словника
def add_student_data(group_number, full_name, course, subjects_grades):
    # Перевірка, чи існує вже запис з таким номером групи
    if group_number in students_dict:
        # Якщо група вже існує, додаємо дані про нового студента
        students_dict[group_number].append({
            'full_name': full_name,
            'course': course,
            'subjects_grades': subjects_grades
        })
    else:
        # Якщо група ще не існує, створюємо новий список студентів
        students_dict[group_number] = [{
            'full_name': full_name,
            'course': course,
            'subjects_grades': subjects_grades
        }]

# Приклад додавання даних про студента до словника
add_student_data(
    group_number='Group1',
    full_name='Іванов Іван Іванович',
    course=2,
    subjects_grades={'Math': 90, 'Physics': 85, 'Chemistry': 80}
)

add_student_data(
    group_number='Group2',
    full_name='Петров Петро Петрович',
    course=1,
    subjects_grades={'Math': 75, 'Physics': 80, 'Chemistry': 70}
)

# Вивід словника
print(students_dict)

# Наступному студенту створити функцію пошуку студента за ПІБ
# ПІБ Хто виконує