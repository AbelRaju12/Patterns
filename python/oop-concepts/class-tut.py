# class is a blueprint for instances

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

# print(emp_1)
# print(emp_2)

emp_1.first = 'Abel'
emp_1.last = 'Raju'
emp_1.email = 'abelraju12@gmail.com'
emp_1.salary = 60000

emp_2.first = 'Gouri'
emp_2.last = 'Varma'
emp_2.email = 'ggv21@gmail.com'
emp_2.salary = 200000       #instances. These negate the actual use of classes.

# print(emp_1.first)
# print(emp_2.salary)

class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + last + '@company.com'
        
emp_1 = Employee('Abel', 'Raju', '60000')
emp_2 = Employee('Gouri', 'Varma', '200000')

# print(emp_1.email)
# print(emp_2.salary)

# print(f"{emp_1.first} {emp_1.last}")

class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + last + '@company.com'
        
    def fullname(self):
        return f"{emp_1.first} {emp_1.last}"
    
emp_1 = Employee('Abel', 'Raju', '60000')
emp_2 = Employee('Gouri', 'Varma', '200000')    

print(emp_1.fullname())

print(Employee.fullname(emp_1))   
