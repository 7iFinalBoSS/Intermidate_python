#itertools :product, permutations,combinations,accumlate, groupby,and infinite itertools
from itertools import product
a = [1,2]
b = [3,4]
prob = product(a,b)
print(list(prob))

from itertools import permutations
a =[1,2,3]
prem = permutations(a)
print(list(prem))

from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))


from itertools import accumulate
import operator
a = [1,2,3,4]
acc = accumulate(a,func = operator.mul)
print(list(acc))

from itertools import groupby
a = [1,2,3,4]

def smaller_than_3(x):
    return x<3
group_obj = groupby(a, key =smaller_than_3)
for key,value in group_obj:
    print(key, list(value))
    
    
from itertools import count, cycle,repeat

a = [1,2,3]
for i in cycle(a):
    print(a)