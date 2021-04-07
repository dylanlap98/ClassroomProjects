from HW11 import *

person = Person()
print(person.get_age())
person.set_age(38)
print(person.get_age())

e = Employee('Dylan', 'Male', 22, '508264', 'Aetna', 95000)
print(e.get_name())

m = Manager('Joshua', 'Male', 25, '459123', 'Aetna', 130000, 'Sr. Data Engineer')
print(m.get_role())

m.set_role('Big Data Engineer Lead')
print(m.get_role())
