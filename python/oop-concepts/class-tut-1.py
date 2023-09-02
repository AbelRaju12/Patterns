class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + last + '@company.com'
        
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.salary = int(self.salary) * 1.25
        
           
emp_1 = Employee('Abel', 'Raju', '60000')
emp_2 = Employee('Gouri', 'Varma', '200000')

# print(emp_1.salary)

# emp_1.apply_raise()

# print(emp_1.salary)

class Employee:
    num_of_emps = 0
    raise_amount = 1.25
    
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + last + '@company.com'
        
        Employee.num_of_emps += 1 #instead of self use Employee since we its indpendent of that particular instance
        
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.salary = int(self.salary) * self.raise_amount

print(Employee.num_of_emps)

emp_1 = Employee('Abel', 'Raju', '60000')
print(Employee.num_of_emps)

emp_2 = Employee('Gouri', 'Varma', '200000')
print(Employee.num_of_emps)

# print(emp_1.__dict__)
# print(Employee.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)

emp_1.raise_amount = 1.5

print(Employee.raise_amount)
print(emp_1.raise_amount)

Employee.raise_amount = 1.5

print(Employee.raise_amount)
print(emp_1.raise_amount)
