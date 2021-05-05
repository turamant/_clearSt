from student_2 import Student


class MyStudent(Student):
    def __init__(self, grupp, name, course, age, iq):
        super().__init__(name, course, age, iq)
        self.grupp = grupp

    @staticmethod
    def print_list_stud():
        for i in MyStudent.list_students2:
            print("Фамилия: ", i.name, "Курс: ", i.course, "Возраст: ",i.age, "Айкю: ", i.iq,"Группа: ", i.grupp)


s = MyStudent(12, "Евлампий", course=2, age=23, iq=102)
s.addStudent()
s = MyStudent(12, "Юрасик", 3, 25, 200)
s.addStudent()

s.print_list_stud()
