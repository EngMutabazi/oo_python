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
    
    @classmethod  # Here we receive a class as our first argument instead self instance
    def set_raise_amount(cls, amount):
        cls.raise_amount= amount
    @classmethod
    def from_string(cls, emp_str):
        firstname, lastname, pay= emp_str.split('-')
        return cls(firstname, lastname, pay)
    def is_work_day(day):
        if day.weekday()==5 or day.weekday()==6:
            return 'Is not a working day'
        return 'Is working day'
    
emp_1= Employee('John', 'Eduin', 600000)
emp_2= Employee('Jacque', 'Milla', 480000)

import datetime
my_date= datetime.date(2022,7,11)
print(Employee.is_work_day(my_date))