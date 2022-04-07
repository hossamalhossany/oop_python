from datetime import date


class Student:

    def __init__(self, name, age):
        self.__name = name  # public  attribute
        self.__age = age  # private attribute

    def describe(self):
        print(f'my name is {self.__name} and my age ==>  {self.__age}')

    @classmethod
    def init_from_brith_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)


a = Student
qq = a.init_from_brith_year('hossam', 1985)
a.describe(qq)


