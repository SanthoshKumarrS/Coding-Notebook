#Lambda arguments = ecpressions

add10 = lambda x: x + 10
#print(add10(5))

#Map Function
a = [1,2,4,5]
b = map(lambda x: x*2, a)
#print(list(b))

#a = [1,2,4,5,6,8]
b1 = filter(lambda x: x%2==0, a)
#print(list(b))

#List Comprehension
c = [x*2 for x in a]
d = [x for x in a if x%2 ==0]
#print(c)

#reduce func
from functools import reduce

e = reduce(lambda x,y: x*y,a)
print(e)