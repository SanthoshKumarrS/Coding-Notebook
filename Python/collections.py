from collections import Counter,namedtuple,deque

a = "aaaaa,bbbb,ffff,cccc,sssss"
my_count = Counter(a)
my_list = list(my_count)
#print(my_list)

Point = namedtuple('Point','x,y,z')
pt = Point(1,2,3)
#print(pt)


#Deque is a double side queue

d = deque()

d.append(1)
d.append(2)
print(d)
d.appendleft(5)
print(d)
d.rotate(1)
print(d)