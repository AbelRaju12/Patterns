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
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
emp_1 = Employee('Abel', 'Raju', '60000')        

Employee.set_raise_amount(1.50)
print(Employee.raise_amount)
print(emp_1.raise_amount)

emp_2 = 'Gouri Varma 70000'
first, last, salary = emp_2.split(" ")
emp_2 = Employee(first, last, salary)

print(emp_2.salary)

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
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, salary = emp_str.split(" ")
        return cls(first, last, salary) #logically Employee(first, last, salary)
    
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# emp_3 = "Abdulla S 850000"

# emp_3 = Employee.from_string(emp_3)

# print(emp_3.first, emp_3.salary)
import datetime
my_date = datetime.date(2023, 10, 2)
print(Employee.is_work_day(my_date))