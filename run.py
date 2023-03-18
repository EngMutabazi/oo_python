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
    
    def apply_raise(self):
        self.pay= int(self.pay * self.raise_amount)
    

emp_1= Employee('John', 'Eduin', 600000)
emp_2= Employee('Jacque', 'Milla', 480000)
emp_1.raise_amount= 1.05

print(Employee.number_of_employee)