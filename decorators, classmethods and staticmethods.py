def bold(smth):
    def inner():
        return "<b>" + smth() + "</b>"
    return inner

def btch_in_the_end(smth):
    def inner(): 
        return smth() + " BTCH"
    return inner


@bold
def hi():
    return "Hello"

print(hi())

@btch_in_the_end
def goodbye():
    return "Bye"

print(goodbye())

"""
Output:
<b>Hello</b>
Bye BTCH
"""

class Employee():
    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self.salary = salary
        self.email = str(name) + "." + str(lastname) + "@gmail.com"

    @classmethod
    def from_string(cls, string):
        # This function is creating an instance from string
        name, lastname, pay = string.split("-")
        return cls(name, lastname, pay)

    @staticmethod
    def is_workday(date):
        # This function is not receiving self or cls as an argument, because it's static
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        return True

# Creating an instance 
emp_1 = Employee("Tim", "Green", 60000)
print(emp_1.email)
print(emp_1.name, emp_1.lastname)
"""
Output:
Tim.Green@gmail.com
Tim Green
"""

emp_2_str = "Jack-Daniels-80000"
emp_2 = Employee.from_string(emp_2_str)
print(emp_2.email)
print(emp_2.name, emp_2.lastname)
"""
Output:
Jack.Daniels@gmail.com
Jack Daniels
"""
import datetime
some_date = datetime.date(2019, 7, 1)
print(Employee.is_workday(some_date))
"""
Output:
True
P.s. Because it's monday.
"""