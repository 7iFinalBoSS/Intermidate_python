# Lists : ordered, mutable, allows duplicate elements

mylist =["banana", "cherry","apple"]
print(mylist)

mylist2 = [5,True,"apple"]
print(mylist2)

item = mylist[2]
print(item)

item = mylist[-1]
print(item)

for i in mylist:
    print(i)
    
if "banana" in mylist:
    print("yes")
else:
    print("NO")
    
print(len(mylist))

mylist.append("lemon")
print(mylist)

mylist.insert(1,"blueberry")
print(mylist)

for i in mylist:
    print(i)
    
item = mylist.pop()
print(item)

print(mylist)

item =mylist.remove("banana")
print(item)

item = mylist.clear()
print(item)

mylist3 = [1,4,5,2,3]

#mylist3.sort()
print(mylist3)

newlist = sorted(mylist3)
print(mylist3)

print(newlist)

mylist = [0]*5
print(mylist)

mylist_2 = [1,2,3,4,5]

new_list = mylist + mylist_2
print(new_list)

##slicing
my_list = [1,2,3,4,5,6,7,8,9]

a = my_list[1:5]
print(a)

b = my_list[::2]
print(b)

list_org = ["banana","cheery","apple"]

list_cpy = list_org

list_cpy.append("lemon")

print(list_cpy)
print(list_org)

mylist = [1,2,3,4,5]
b = [x*x for x in mylist]

print(mylist)
print(b)

