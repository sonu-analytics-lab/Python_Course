class Employee:
    company = "Asus"  # this is class attribute

    def __init__(self, salary, name, bond, company):
        self.salary = salary  # instance attribute
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(
            f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is {self.bond} years.")


e1 = Employee(3400, "John", 3, "Tesla")
print(e1.company)  # it will always print instance attribute

# print(Employee.company) # This is always print the class attribute

# object introspection
print(dir(e1))
