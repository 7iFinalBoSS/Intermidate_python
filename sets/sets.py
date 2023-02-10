#sets : unordered, mutable, no duplicate
myset = set([1,2,3,4])
print(myset)

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

myset.remove(3)
myset.discard(2)
myset.clear()
print(myset)

myset.add(1)
myset.add(2)
myset.add(3)

print(myset)

for i in myset:
    print(i)
    
if 1 in myset:
    print("yes")
    
odds = {1,3,5,7,9}
evens ={0,2,4,6,8}
primes ={2,3,5,7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

print(setA.issubset(setB))


diff = setB.difference(setA)
print(diff)

diff = setA.symmetric_difference(setB)
print(diff)

setA.update(setB)
print(setA)