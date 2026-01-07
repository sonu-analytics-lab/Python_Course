# CLASS: class is blueprint or template. eg form of exam that contains, Name, age electives
# father's name

# Objects ; Specfic instance created form the template (class).
# Eg. form which conatain the data for john Doe

class Employee:
    company = 'HP'

    # self is imp here because self is way  to reference the object of the clas which is being crated.
    def get_salary(self):
        return 34000


e = Employee()  # An obect of class employee is created here
print(e.get_salary())  # employee e's get salary method is called
