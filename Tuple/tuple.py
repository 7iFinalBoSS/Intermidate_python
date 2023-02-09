# Tuple : ordered, immutable, allows duplicate elements

mytuple = tuple(["max",28,"Boston"])
print((mytuple))

item = mytuple[0]

print(item)

for i in mytuple:
    print(i)
    
if "max" in mytuple:
    print("yes")
else:
    print("No")
    
my_tuple= ('a','p','p','l','e')

print(my_tuple.count('p'))

print(my_tuple.index('a'))

#print(my_tuple.index('0'))

my_list = list(my_tuple)

print(my_list)

my_tuple_2 = tuple(my_list)
print(my_tuple_2)

a = (1,2,3,4,5,6,7,8,9,10)

b = a[2::1]

print(b)

b = a[-1]
print(b)

my_tuple = "max",28,"boston"

name,age,city = my_tuple
print(name)
print(city)
print(age)

my_tuple = (0,1,2,3,4)

i1,*i2, i3 = my_tuple

print(i1)
print(i2)
print(i3)

import sys
my_list =[0,1,2,"hello",True]
my_tuple = (0,1,2,"hello",True)
print(sys.getsizeof(my_list),"bytes")
print(sys.getsizeof(my_tuple),"bytes")
