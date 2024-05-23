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

#Batrachenko Serhii
def find_student_by_full_name(full_name):
    # Перебір груп та студентів у словнику
    for group_number, students in students_dict.items():
        # Перебір студентів у групі
        for student in students:
            # Перевірка чи співпадає введений ПІБ з ПІБ студента
            if student['full_name'] == full_name:
                return {
                    'group_number': group_number,
                    'full_name': student['full_name'],
                    'course': student['course'],
                    'subjects_grades': student['subjects_grades']
                }
    # Якщо студента не знайдено, повертаємо None
    return None

# Приклад використання функції пошуку студента за ПІБ
student_info = find_student_by_full_name('Іванов Іван Іванович')
if student_info:
    print("Знайдено студента:")
    print(student_info)
else:
    print("Студента не знайдено.")

#Створити функцію видалення даних про студента
#Fomin Vladyslav
    
def delete_student(full_name):
    # Перебір груп та студентів у словнику
    for group, students in students_dict.items():
        # Перебір студентів у групі
        for student in students:
            # Перевірка чи співпадає введений ПІБ з ПІБ студента
            if student['full_name'] == full_name:
                # Якщо студент знайдений, видаляємо його зі списку студентів
                students.remove(student)
                print(f"Дані про {full_name} успішно видалені")
                return
    # Якщо студента не знайдено, виводимо повідомлення
    print(f"Студент {full_name} не знайдений в базі даних")

# Приклад використання функції видалення даних про студента
delete_student('Іванов Іван Іванович')

#Leonid Raiev
# Функція для пошуку студентів за оцінками
def find_students_by_grade(subject, min_grade):
    found_students = []
    # Перебір груп та студентів у словнику
    for group_number, students in students_dict.items():
        # Перебір студентів у групі
        for student in students:
            # Перевірка чи є у студента потрібний предмет та чи оцінка не менше мінімальної
            if subject in student['subjects_grades'] and student['subjects_grades'][subject] >= min_grade:
                found_students.append({
                    'group_number': group_number,
                    'full_name': student['full_name'],
                    'course': student['course'],
                    'subjects_grades': student['subjects_grades']
                })
    return found_students

# Приклад використання функції пошуку студентів за оцінками
students_with_high_math_grades = find_students_by_grade('Math', 80)
print("Студенти з оцінкою з математики не менше 80:")
for student in students_with_high_math_grades:
    print(student)



    