names = ['sha', 'sha0', 'sha1', 'sha2']
# normal loop for list
for name in names:
    print(name+' arora')
#using List comprehensions
name_list = [name+' arora1' for name in names]
print(name_list)
#conditional list comprehensions
expediture_list = [23,123,112,234,500,1221,4566,22473]
excess_expediture = [item for item in expediture_list if item>=500]
print(excess_expediture)
# list containing dictionaries
students = [{'name': 'abd', 'age':28}, {'name': 'xyz', 'age':31}]
student_name = [student.get('name') for student in students]
print(student_name)
# list containing lists
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat = [x for row in matrix for x in row]
print(flat)
# enumerate over range
companies = ['TCS', 'Projectplace', 'Troux', 'Planview']
for i, company in enumerate(companies):
    print(i, company)