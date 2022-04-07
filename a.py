class Student:
    no_of_student = 0  # class attribute

    def __init__(self, name, age, courses):
        self.__name = name  # public  attribute
        self.age = age # private attribute
        self.courses = courses
        Student.no_of_student += 1  # here we use class attribute, so we must use class name first

    def describe(self):
        print(f'my name is {self.name} and my age ==>  {self.age}')

    def is_old(self, num):
        if  self.age <= num:
            print(f'this student {self.name} has age ==> {self.age} is not old than {num}')
        else:
            print(f'this student {self.name} has age ==> {self.age} is  old of {num}')

    def get_name(self):
        return print(self.__name)

    def set_name(self, name):
        self.__name = name


a = Student('hossam', 25, 'html')
b = Student('waleed', 30, 'css')
c = Student('ahmed', 35, 'java')

# b.describe()
# c.is_old(10)

a.set_name('ali')
a.get_name()