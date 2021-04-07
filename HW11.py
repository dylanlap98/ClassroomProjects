class Person:

    def __init__(self, name, gender, age):
        self.__name = name
        self.__gender = gender
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age


class Employee(Person):

    def __init__(self, name, gender, age, employee_id, company, salary):
        Person.__init__(self, name, gender, age)
        self.__employee_id = employee_id
        self.__company = company
        self.__salary = salary

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_company(self, company):
        self.__company = company

    def set_salary(self, salary):
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def get_company(self):
        return self.__company

    def get_salary(self):
        return self.__salary


class Manager(Person):

    def __init__(self, name, gender, age, role):
        Person.__init__(self, name, gender, age)
        self.__role = role

    def set_role(self, role):
        self.__role = role

    def get_role(self):
        return self.__role



