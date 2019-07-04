class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print("First & last has been deleted!")

    @property
    def email(self):
        return self.first + '.' + self.last + '@email.com'


emp_1 = Employee("John", "Smith")

emp_1.first = "George"

print(emp_1.email)
print(emp_1.fullname)
# George.Smith@email.com
# George Smith
emp_1.fullname = "Corey Schafer"
print(emp_1.first, emp_1.email)
# Corey Corey.Schafer@email.com
del emp_1.fullname
# First & last has been deleted!
print(emp_1.first, emp_1.last)
# None None
