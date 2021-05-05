class Student:
    """Структура"""
    list_students2 = []
    def __init__(self,  name="name", course=0, age=0, iq=0):
        self.name = name
        self.course = course
        self.age = age
        self.iq = iq


    def addStudent(self):
        """ Добавим в список студента"""
        self.list_students2.append(self)

    @staticmethod
    def print_list_stud():
        """ извлечение из списка всех студентов"""
        for i in Student.list_students2:
            print("X^", i.name, i.age)


if __name__=="__main__":

    st = Student("Иванов", 2, 23, 105)
    st.addStudent()

    st2 = Student("Петров", 3, 21, 107)
    st2.addStudent()

    Student.print_list_stud()

