#Generators
#Generators are memory efficient,they save a lot of memory while working with large data

def my_gen(num):
    print("Hello")
    while num > 0:
        yield num
        num -= 1

#cd = my_gen(3)

def fibonacci(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b

#fib = fibonacci(25)
#for i in fib:
#    print(i)

#Generator Objects are written in parenthesis in list comprehension instead of Square Brackets
import sys
mygenerator = (i for i in range(1000000) if i%2==0)
print(sys.getsizeof(mygenerator)) # = 200 Generators are Memory efficient

mylist = [i for i in range(1000000) if i%2==0]
print(sys.getsizeof(mylist)) # = 4167352