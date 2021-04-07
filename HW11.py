# The variables in these objects are (mostly) all going to be private


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


class Client(Person):

    def __init__(self, name, gender, age, client_id, date_started):
        Person.__init__(self, name, gender, age)
        self.__client_id = client_id
        self.__date_started = date_started

    def set_client_id(self, client_id):
        self.__client_id = client_id

    def set_date_started(self, date_started):
        self.__date_started = date_started

    def get_client_id(self):
        return self.__client_id

    def get_date_started(self):
        return self.__date_started

# END-----------------------------------------------------------
