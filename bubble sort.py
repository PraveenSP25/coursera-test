def sort(num):
    for i in range(len(num)-1, 0, -1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp

num=[2,3,7,6,1,9]
sort(num)
print(num)