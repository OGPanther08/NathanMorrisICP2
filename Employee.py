#employee class
class Employee:
    #employee count and total salary to calculate average salary
    employee_count = 0
    total_salary = 0

    #Constructor
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        #increments employee count and adds the salary to total salary
        Employee.employee_count += 1
        Employee.total_salary += salary


    #calculates average salary
    @classmethod
    def average_salary(cls):
        if cls.employee_count > 0:
            return cls.total_salary / cls.employee_count
        return 0
    
    def __str__(self):
         return f"Employee: {self.name}, Department: {self.department}, Salary: {self.salary}"

#Fulltime Employee class
class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        #calls the parent class contructor
        super().__init__(name, family, salary, department)

    def __str__(self):
        return f"Fulltime Employee: {self.name}, Department: {self.department}, Salary: {self.salary}"


# Creating instances of Employee and FulltimeEmployee
emp1 = Employee('Alice', 'Smith', 50000, 'HR')
emp2 = Employee('Bob', 'Johnson', 60000, 'Finance')

ft_emp1 = FulltimeEmployee('Charlie', 'Brown', 70000, 'Engineering')
ft_emp2 = FulltimeEmployee('Daisy', 'Miller', 80000, 'Marketing')

# Printing the details of each employee
print(emp1)
print(emp2)
print(ft_emp1)
print(ft_emp2)

# Calculating and printing the average salary of all employees
print("Average Salary of all employees:", Employee.average_salary())

# Printing the total number of employees
print("Total number of employees:", Employee.employee_count)
