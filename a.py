class Student:
    no_of_student = 0  # class attribute

    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses
        Student.no_of_student += 1


a = Student('hossam', 25, 'html')
b = Student('waleed', 30, 'css')



print(Student.no_of_student)
