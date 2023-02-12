#collections : Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

a = "aaaabbbbccc"
my_counter = Counter(a)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(list(my_counter.elements()))

from collections import namedtuple
Point = namedtuple('point','x,y')
pt = Point(1, -4)
print(pt.x, pt.y)

from collections import OrderedDict
Ordered_Dict = OrderedDict()
Ordered_Dict['a'] =1
Ordered_Dict['b'] =2
Ordered_Dict['c'] =3
Ordered_Dict['d'] =4

print(Ordered_Dict)

from collections import defaultdict
d  = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)


from collections import deque
d = deque()

d.append(1)
d.append(2)
print(d)


my_list = [1,2,3,4,5,6]
d = deque()
for i in my_list:
    d.append(i)
    
d.rotate(3)
print(d)