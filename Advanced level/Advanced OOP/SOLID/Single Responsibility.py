'''
Single responsibility
    Each class is responsible for only one thing and should have only one reason to change
    More than one responsibility is called coupling (обвързаност)
'''

# Violation
'''
This class is responsible for two things:
    - keep data for the student
    - save data in database
'''


class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def register(self, student):
        pass

    def unregister(self, student):
        pass


# the right way

class Student1:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class StudentRegistry:
    def __init__(self):
        self.students = []

    def register(self, student):
        self.students.append(student)

    def unregister(self, student):
        self.students.pop(self.students.index(student))


student = StudentRegistry()

student.register(Student('Gosho'))
