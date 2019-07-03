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

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.fullname()} --> {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)
# Output (before defining __str__): Employee('Corey', 'Schafer', 50000)
# Output (after defining __str__): Corey Schafer --> Corey.Schafer@email.com
print(repr(emp_1))
print(str(emp_1))
"""
Output:
Employee('Corey', 'Schafer', 50000)
Corey Schafer --> Corey.Schafer@email.co
"""
print(emp_1+emp_2)
# Output: 110000

print(len("test")) # 4
print("test".__len__()) # 4

print(len(emp_1)) # 13