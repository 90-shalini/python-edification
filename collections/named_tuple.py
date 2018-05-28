from collections import namedtuple

# light weight object type
#  like dictionaries they have keys that are hashed to a particular values, but it supports access
# from both key values + iteration
# Access by index/name, key value, getattr

employee = namedtuple('employee', ('name', 'company'))
employee.__new__.__defaults__ = (None, None)

e = employee('shalini', 'TCS')
e2 = employee('Vibhor', 'cisco')

print(e)
print(e2.company)