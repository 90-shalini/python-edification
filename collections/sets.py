s = {1,2,3,4}
#SETS: like mathematical sets
# do not have duplicate values, no particular order
# no accessing using index
s1 = set({1,2,3,4})
# if u will add muliple values, it will get created using distinct values
#Accessing Sets
for items in s:
    print(s)
# we can remove duplicated in list bu pottung it into sets and get length for the same
alp = ['a', 'b', 'c', 'a', 'b']
print("list of distincts alps", list(set(alp)))
print("Length of distinct alphabets:", len(set(alp)))
#SET Methods
#add
s.add('122')
print("After adding: ", s)
#if number is present, return nothing and do nothing
# s.remove('3')
print("After Removing:", s)
# remove will throw error if item is not present, use Discard
s.discard('3')
#Copy, similar to other collections
s1 = s.copy()
print("copied:", s1)
s1.clear()
print(s1)

# Set Math functions, e.g Union, Intersection
# Union |
# intersection &

#Set comprehensions
set_c = {x**2 for x in range(0,11)}
print("Set comprehension", set_c)
# can add condition in set comprehension similar to other collections


