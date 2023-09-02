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
    
emp_1 = Employee('Abel', 'Raju', '60000')    
    
class Developer(Employee):
    pass

dev_1 = "Sybil AJcob 55000"
dev_1 = Developer.from_string(dev_1)

# print(dev_1.salary)
# print(dev_1.email)

# print(help(Developer))

print(dev_1.salary)
Developer.set_raise_amount(1.8) #doesnt change amount for Employee
dev_1.apply_raise()
print(dev_1.salary)
print(Employee.raise_amount)

class Developer(Employee):
    def __init__(self, first, last, salary, lang):
        super().__init__(first, last, salary) #inhertied from prev
        # Employee.__init__(self, first, last, salary) #or like this
        self.lang = lang

dev_1 = Developer('Sybil', 'Jacob', 55000, 'Java')
print(dev_1.lang)

class Manager(Employee):
    def __init__(self, first, last, salary, employees = None):
        super().__init__(first, last, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_employee(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
            
mgr_1 = Manager('Sara', 'Smith', 90000, [dev_1])

print(mgr_1.print_emps())

print(issubclass(Manager, Employee))