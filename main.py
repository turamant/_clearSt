counter_student = 0
student_list = []

def add_student(nm, course, age):
    student = {}
    student["Фамилия: "] = nm
    student["курс: "] = course
    student["Возраст: "] = age
    global counter_student
    counter_student += 1
    return student



if counter_student < 3: student_list.append(add_student("Виталий", 2, 54))
if counter_student < 3: student_list.append(add_student("Иван", 1, 18))
if counter_student < 3: student_list.append(add_student("Сергей", 2, 23))
if counter_student < 3: student_list.append(add_student("Лоля", 3, 24))
if counter_student < 3: student_list.append(add_student("Света", 1, 17))
else:
    print("Прием закончен")

for stud in student_list:
    print(stud)

print(counter_student)
