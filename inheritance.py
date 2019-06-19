"""Example of inheritance."""
# https://www.ibiblio.org/g2swap/byteofpython/read/inheritance.html
# !/usr/bin/python
# Filename: inherit.py


class SchoolMember(object):
    """Represents any school member."""

    def __init__(self, name, age):
        """Initialize."""
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {}'.format(self.name))

    def tell(self):
        """Tell my details."""
        print('Name:"{}" Age:"{}"'.format(self.name, self.age))


class Teacher(SchoolMember):
    """Represents a teacher."""

    def __init__(self, name, age, salary):
        """Initialize."""
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {}'.format(self.name))

    def tell(self):
        """Tell my details."""
        SchoolMember.tell(self)
        print('Salary: "{}"'.format(self.salary))


class Student(SchoolMember):
    """Represents a student."""

    def __init__(self, name, age, marks):
        """Initialize."""
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {}'.format(self.name))

    def tell(self):
        """Tell my details."""
        SchoolMember.tell(self)
        print('Marks: "{}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

print()  # prints a blank line

members = [t, s]
for member in members:
    member.tell()  # works for both Teachers and Students
