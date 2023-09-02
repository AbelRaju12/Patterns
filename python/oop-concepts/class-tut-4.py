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
        
    def __repr__(self):
        return f"Employee {self.email} {self.salary}"
    def __str__(self):
        return f"Employee {self.fullname()} {self.salary}"

    def __add__(self, other):
        return int(self.salary) + int(other.salary)
    
    def __len__(self):
        return len(self.fullname())
    
    
emp_1 = Employee('Abel', 'Raju', '60000')
emp_2 = Employee('Gouri', 'Varma', '200000') 

print(emp_1.__repr__()) #instead of object it will print the details required as specified
print(emp_1.__str__()) 

print(int.__add__(4,6))
print(str.__add__('1','2'))

print(emp_1 + emp_2) #if no __add__ then it will return error

print(len(emp_1)) #'abel'.__len__() is actually len('abel')