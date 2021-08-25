'''

Classes, modules and functions should be open for extension, but closed for modifications
or if we want to change the behavior of the class we shouldn't change any other code

    This can be achieved through:

        - Abstraction
        - Mix-ins
        - Monkey-Patching (modified a method without adding it)
        - Generic functions (using overloading)

'''
# Violation
from abc import ABC, abstractmethod

'''
If we want to extend our behavior we have to modify the get_discount method adding additional if.
we can resolve this problem using abstraction
'''


class StudentTaxes:
    def __init__(self, name, semester_fee, average_grade):
        self.name = name
        self.semester_fee = semester_fee
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade >= 5:
            return self.semester_fee * 0.4
        elif self.average_grade >= 4:
            return self.semester_fee * 0.3


class StudentTaxes1(ABC):
    def __init__(self, name, semester_fee, average_grade):
        self.name = name
        self.semester_fee = semester_fee
        self.average_grade = average_grade

    @abstractmethod
    def get_discount(self):
        pass


class ExcellentStudent(StudentTaxes1):

    def get_discount(self):
        return self.semester_fee * 0.4


class GoodStudent(StudentTaxes1):

    def get_discount(self):
        return self.semester_fee * 0.3