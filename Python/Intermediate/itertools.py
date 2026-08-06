from itertools import product,permutations,combinations,accumulate,groupby,count,cycle,repeat

a = [1,2,3,4]
b = [1,5,6,9]

prod = product(a,b)
#print(list(prod))

perm = permutations(a, 2)
#print(list(perm))

comb = combinations(a, 2)
#print(list(comb))

acc = accumulate(a)
#print(list(acc))

grp_obj = groupby(b, key= lambda x: x > 5)
for key,value in grp_obj:
    print(key,list(value))


for i in repeat(5, 15):
    print(i)