class Employee:
    number_of_employee=0
    raise_amount=1.04
    def __init__(self, first_name, last_name, pay):
        self.first_name= first_name
        self.last_name= last_name
        self.pay= pay
        Employee.number_of_employee +=1

    @property
    def email(self):
        return'{}.{}@gmail.com'.format(self.first_name, self.last_name)
    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
emp_1= Employee('John', 'Smith', 5000)

emp_1.first_name= 'jimy'
print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname)


