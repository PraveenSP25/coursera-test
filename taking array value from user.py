from array import*
arr=array('i',[])
n=int(input("enter the length of array"))
for i in range(n):
    a=int(input("enter the next values"))
    arr.append(a)
print(arr)
k=0
val=int(input("enter a value for search"))
for e in arr:
    if e==val:
        print(k)
        break
    k=k+1
print((arr.index((val))))
