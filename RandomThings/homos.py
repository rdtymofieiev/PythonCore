class Employee:
    counter = 0
    def __init__(self,name,salary):
        Employee.counter += 1
        self.__name = name 
        self.__salary = salary
    
    def displayTotal(self):
        return f"Total Employee {Employee.counter}"
    
    def displayEmployee(self):
        return f"Name : {self.__name},  Salary: {self.__salary}"
    
    def __del__(self):
        Employee.counter -= 1
        
        
#####################################
emp1 = Employee("Liubov", 350)
emp2 = Employee("Vasyl", 600)
emp3 = Employee("Liubomyr", 270)
#######################################
print(Employee.counter)
print(emp1.displayTotal())
print(emp3.displayEmployee())
#########################################
print(f"Employee.doc:{Employee.__doc__}")
#print(f"Employee.name:{Employee.name}")
#print(f"Employee.module:{Employee.module}")
#print(f"Employee.bases:{Employee.bases}")
#print(f"Employee.dict:{Employee.dict}")
        