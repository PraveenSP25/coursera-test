

nums = [2,3,4,5,6,7]
evens = list(filter(lambda n: n%2==0, nums))
print(evens)
doubles=list(map(lambda a: a*2, evens))
print(doubles)
from functools import reduce
sum=reduce(lambda a,b: a+b, doubles)
print(sum)