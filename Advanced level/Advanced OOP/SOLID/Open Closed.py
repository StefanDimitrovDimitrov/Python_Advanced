'''

Classes, modules and functions should be open for extension, but closed for modifications
or if we want to change the behavior of the class we shouldn't change any other code

    This can be achieved through:

        - Abstraction
        - Mix-ins
        - Monkey-Patching (modified a method without adding it)
        - Generic functions (using overloading)

'''

class StudentTaxes:
    def __init__(self,name, semester_fee,average_grade):
        pass