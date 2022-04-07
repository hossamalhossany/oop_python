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


class Pizza:
    def __init__(self, ing):
        self.ing = ing

    def __str__(self):
        return f'pizza contain  is{self.ing} '

    @classmethod
    def veg(cls):
        return cls(['a', 'b', 'c'])

    @classmethod
    def bbb(cls):
        return cls(['d', 'f'])


p1 = Pizza(['y', 'ooo'])

p2 = Pizza.veg()

p3 = Pizza.bbb()

print(p1)
print(p2)
print(p3)


