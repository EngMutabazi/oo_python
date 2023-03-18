class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name= first_name
        self.last_name= last_name
        self.pay= pay
    
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
emp_1= Employee('John', 'Eduin', 600000)
print(emp_1.fullname())