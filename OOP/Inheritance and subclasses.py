class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


emp_1 = Employee("James", "Bond", 50000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
"""
Output:
50000
52000
"""

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev_1 = Developer("John", "Wick", 70000, "Python")
print(dev_1.fullname())
print(dev_1.raise_amt)
print(dev_1.prog_lang)
"""
Output:
John Wick
1.1
Python
"""

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
"""
Output:
70000
77000
"""

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        if len(self.employees) == 0:
            print(f"There are no employees working under the supervision of the manager {self.fullname()}")
        else:
            print(f"Employees under the supervison of the manager {self.fullname()}")
            for emp in self.employees:
                print("-->", emp.fullname())

mng_1 = Manager("Sue", "Smith", 90000, [dev_1])
print(mng_1.email)
# Sue.Smith@email.com

mng_1.print_emps()
mng_1.add_emp(emp_1)
mng_1.print_emps()
mng_1.remove_emp(emp_1)
mng_1.remove_emp(dev_1)
mng_1.print_emps()
"""
Output:
Employees under the supervison of the manager Sue Smith
--> John Wick
Employees under the supervison of the manager Sue Smith
--> John Wick
--> James Bond
There are no employees working under the supervision of the manager Sue Smith
"""


print(isinstance(Manager, Employee))
# False
print(isinstance(emp_1, Employee))
# True
print(isinstance(mng_1, Manager))
# True
print(issubclass(Developer, Employee))
# True
print(issubclass(Manager, Developer))
# False