def sort(num):
    for i in range(len(num)):
        minpos=i
        for j in range(i,len(num)):
            if num[minpos] > num[j]:
                minpos= j
        temp=num[i]
        num[i]=num[minpos]
        num[minpos]=temp
        print(num)
num=[5,4,3,7,8,2]
sort(num)
print(num)

