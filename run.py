class Employee:
    number_of_employee=0
    raise_amount=1.04
    def __init__(self, first_name, last_name, pay):
        self.first_name= first_name
        self.last_name= last_name
        self.pay= pay
        self.email= first_name + '.'+ last_name + '@gmail.com'
        Employee.number_of_employee +=1
    
    def personal_informations(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.email)
    
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def apply_raise(self):
        self.pay= int(self.pay * self.raise_amount)
    def __repr__(self): # is used for debugging and loging (recreate object)
        return "Employee('{}','{}', '{}')".format(self.first_name, self.last_name, self.pay)
    
    def __str__(self): # is used as a display to enduser
        return '{}-{}'.format(self.fullname(),self.email)
    
    def __add__(self, other):
         return self.pay + other.pay
    
emp_1= Employee('John', 'Eduin', 600000)
emp_2= Employee('Jacque', 'Milla', 480000)



print(emp_1+emp_2)
# print(repr(emp_1))
# print(str(emp_1))
# print(emp_1.__repr__())
# print(emp_1.__str__())
