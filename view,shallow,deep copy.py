### shallow copy

from numpy import *
arr1=array([2,3,4,5])
arr2=arr1.view()
arr1[2]=5
print(arr1)
print(arr2)

###deep copy
from numpy import *
arr1=array([2,3,4,5])
arr2=arr1.copy()
arr1[2]=5
print(arr1)
print(arr2)