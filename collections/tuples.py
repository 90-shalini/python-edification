# Tuples: group of items
num = (1,2,3,4)
# IMUTABLE: you can't update them like a list
print(3 in num)
# num[1] = 'changed' # will throw error
# Faster than list, for the data which we know we will not change use TUPLE
# tuple can be a key on dictionary
# creating/accessing -> () or tuple
xyz = tuple(('a', 'b'))
print("tuple created using tuple: ", xyz)
#dictionary.items() returns a tuple of key:value in dictionary
months = ('Jan', 'Feb', 'March', 'April', 'June', 'July', 'Aug')
#ITERATING over tuples, using loops
for month in months:
    print(month)
#Tuple Methods:
counting = (1,2,3,4,5,3,4,5,6,4,5,3,6)
#count
print('Count of element passed in function: ', counting.count(5))
#index
print("Index of element:", counting.index(3))
# Nested tuples
# can do slicing like lists


