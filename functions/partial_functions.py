from functools import partial

def func(x,y,z,a):
    return x*4 + y*3 + z*2 +a

partial_results = partial(func, 6,6,6)

print(partial_results(6))

# a partial function is useful for : making N arguement functions callable using fewer arguments, as in above func
# normal function expects 4 parameters, we turned into partial and then lastle we gave the final required ARGUMENTS

def spam(a, b, c, d):
    print(a,b,c,d)

result1 = partial(spam, 1, 2, 3)
result1(4)

result1(d=23)

result2 = partial(spam, 3, b=12)
result2(c=4,d=5)

result3 = partial(spam, 3, 12)
result3(34,334)

#partials() fixes the values for certain arguments and create a new callables i.e. Result..
#and this new callable accept the remaining/unassigned arguments, combines it with previous arguments and pass to original funtiion

