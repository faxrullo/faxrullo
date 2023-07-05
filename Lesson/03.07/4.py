import os
os.system("cls")
class Employee: 
    def __init__(self):
        self._emp_name=None
        self._emp_id=None
        self._emp_salary=None
        self._emp_department=None
        self._employees=list()

    def sign_up(self):
        print("Entering employee information")
        self._emp_name=input("Enter employee name: ")
        self._emp_id=input("Enter employee id: ")
        self._emp_department=input("Enter employee department: ")
        self._emp_salary=int(input("Enter employee salary: "))
        self._employees.append([self._emp_name,self._emp_id,self._emp_salary,self._emp_department])
    
    def print_employee_detail(self):
        print("View employee information")
        id=input("Enter employee id: ")
        for x in self._employees:
            if x[1]==id:
                print(f"Employee name: {x[0]}\nEmployee id: {x[1]}\nEmplyee salary: {x[2]}\nEmployee department: {x[3]}")
    
    def emp_assign_department(self):
        print("Changing the employee's position")
        id=input("Enter employee id: ")
        new_department=input("Enter employee new department: ")
        for x in self._employees:
            if x[1]==id:
                self._employees[0][3]=new_department
    
    def calculate_emp_salary(self):
        print("Calculating the employee's salary")
        id=input("Enter employee id: ")
        hours_worked=int(input("Enter employee hours worked: "))
        for x in self._employees:
            if x[1]==id and hours_worked>50:
                over_time=hours_worked-50
                over_time_amount=(over_time*(x[2]/50))+x[2]
                self._employees[0][2]=over_time_amount
                
    
emp=Employee()
emp.sign_up()
emp.print_employee_detail()
emp.calculate_emp_salary()
emp.emp_assign_department()
emp.print_employee_detail()
