from array import *
val = array('i', [2, 3, 4, 6, 8, 1])
temp = 0
print("orginal array")
for i in range(0, len(val)):
    print(val[i], end="")
for i in range(0,len(val)):
    for j in range(i + 1, len(val)):
        if (val[i] > val[j]):
            temp=val[i]
            val[i]=val[j]
            val[j]=temp
print()
print("Elements of array sorted in ascending order: ")
for i in range(0, len(val)):
    print(val[i], end=" ")

