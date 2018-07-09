names = ['sha', 'sha0', 'sha1', 'sha2']
#accessing list
print(names[0],'Reverse List: ', names[-1], names[-2])
# normal loop for list, list can have values of multiple type(string, int, boolean)
for name in names:
    print(name+' arora')

#List methods
data = [1,2,3,4,4,5,6]
#APPEND: takes only 1 arguement
data.append('shalini') 
#EXTEND:add all items
data.extend('abc')
data.extend([7,8,9,10]) 
#Insert: inserts value at position
data.insert(0, 'name') 
data.insert(len(data), 'LAST')
print('List methods:', data)
# POP: returns removed item, and indexError if req
removed_item = data.pop() 
print('Removing last item', data)
print('removed item', removed_item)
data.pop(1)
print('removing from index', data)
# REMOVE: remove based on value, throws error if value not present, remove first if multiple entries
# doesn't return value
data.remove('shalini') 
print('After all:', data)
#INDEX: gives the index of element in list, gives first position if multiple values
print('Index of name:', data.index('name'))
# can specify start and end if, multiple values
#COUNT: return number of times an element occured in list
print('Count of 4 : ',data.count(4))
#REVERSE: reverse the order of list, and doesn't return anything..just change the list itself
data.reverse()
print('Reverse list:', data)
#SORT ; sort in ascending by default, will work on lits of same types...and doesn't return anything..just change the list itself
names_list = ['shalini', 'Arora', 'vibhor', 'Jain']
names_list.sort()
print('Sorted list:', names_list)
#JOIN: string method : it takes list..concatenate them and make a single string
words = ['coding', 'is', 'fun']
print("Sentence:", '.'.join(words))


#SLICING
data = [1,2,3,4,5,6,7,8,9]
print(data[1:])
print(data[9:])
print(data[0:]) # copy of list
print(data is data[0:])
print(data[-2:])

#end
print(data[:2])
print(data[2:6])
#step
print(data[1::2])
# Reverse , modify using slicing
#swapping values, for shuffling, sorting, 


#using List comprehensions
name_list = [name+' arora1' for name in names]
print('List Comprehensions:', name_list)
#conditional list comprehensions
expediture_list = [23,123,112,234,500,1221,4566,22473]
excess_expediture = [item for item in expediture_list if item>=500]
print(excess_expediture)
# list containing dictionaries
students = [{'name': 'abd', 'age':28}, {'name': 'xyz', 'age':31}]
student_name = [student.get('name') for student in students]
print(student_name)
# enumerate over range
companies = ['TCS', 'Projectplace', 'Troux', 'Planview']
for i, company in enumerate(companies):
    print(i, company)


# list containing lists :Nested List comprehensions
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat = [x for row in matrix for x in row]
print(flat)

coord = [[12.44, 23.44], [76.65, 45.556], [57.86, 99.22]]
[[print(coordinates) for coordinates in loc] for loc in coord]
#NOTE: lists can't be the key in dictionary, it will throw unhashable error
