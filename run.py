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
    
class Developer(Employee):
    raise_amount=1.10
    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang= prog_lang

class Manager(Employee):
    def __init__(self, first_name, last_name, pay, employees= None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees= []
        else:
            self.employees= employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())     

dev_1= Developer('John', 'Eduin', 600000, 'python')
dev_2= Developer('Jacque', 'Milla', 480000, 'c++')

mngr_1= Manager('king','smith', 105000,[dev_1])

print(isinstance(mngr_1, Developer))
print(issubclass(Manager, Developer))
print(issubclass(Developer, Employee))