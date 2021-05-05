list_students_2 = []

class Student:
    """Структура"""
    counter_student = 0
    def __init__(self):
        self.student = {}
        Student.counter_student += 1

    def add_new_student(self, name="", course="", age=0, iq=0):
        self.student["Фамилия"] = name
        self.student["Курс"] = course
        self.student["Возраст"] = age
        self.student["Ай-кью"] = iq
        list_students_2.append(self.student)


    @staticmethod
    def student_counting():
        return Student.counter_student

gruppa = ['Иванов','Петров','Баширов','Королев','Гагарин',
          'Петькин','Васькин','Лукьянов','Васильев','Николаев']


def generating_students(grupps):
    for i in range(len(grupps)):
        st = Student()
        st.add_new_student(name=grupps[i], course=i+1, age=i+15, iq=i+100)
    print("Всего студентов: ", st.student_counting())

if __name__=="__main__":
    generating_students(gruppa)
    for st2 in list_students_2:
        for k, v in st2.items():
            print(k, ":", v)




