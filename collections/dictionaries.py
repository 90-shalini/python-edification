#key value pairs, 2 ways to create a dictionary
employee = {'name': 'shalini', 'exp': 6, 'skills':["core Java", "Python", "Selenium"]}
company = dict(name="Planview")
print(employee, company)
#accessing value
print(employee['name'])
print(employee.values()) # returns a list of values
print(employee.keys())# returns a list of keys
# .Items()
for k, v in employee.items():
    print("Key is {} ".format(k) + "Values are {}".format(v))
print('name' in employee) # for keys or employee.keys()
print('shalini' in employee.values())

# Dictionary methods
#CLEAR
d = dict(a=1, b=2)
c = d.copy()
print(d)
print(c)
print("checks the values:", c==d)
print("Checks the memory reference:",c is d)
d.clear()
print(d)
#FROMKEYS: create key-value pairs from comma seprated values, new dictionary
#iterates over first parameter and assign second parameter to each eleemtn in 1st parameter
print({}.fromkeys(['email', 'id', 'name'], 'unknown'))
# GET, return value of passed key else None
print(employee.get('name'))
# POP, remove key:value, is key exisits else error
print(employee.pop('exp'))
# POPITEM
print(employee.popitem())
print(employee)
# UPDATE: add new k:v and overwrite existing keys
employee.update({'name': 'shalini', 'exp': 6})

#Dictionary COMPREHENSIONS
print({num: num**2 for num in [1,2,3,4]})
# can add conditional logics in the same
# can use dict directly to make dictionary after some operation
