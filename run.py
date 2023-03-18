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
        first_name, last_name, pay= emp_str.split('-')
        return cls(first_name, last_name,pay)


emp_1= Employee('John', 'Eduin', 600000)
emp_2= Employee('Jacque', 'Milla', 480000)

emp_str1= 'john-doe-5000'
emp_str2= 'steve-smith-1000'
emp_str3= 'jeanette-song-1500'
newemp= Employee.from_string(emp_str1)

print(newemp.email )
print(newemp.pay )

