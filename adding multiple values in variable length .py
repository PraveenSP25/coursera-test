
def sum(a,*b): #or we take only *b and c= 0 then ans is same

    c = a
    for i in b:
        c = c+i
    print(c)
sum(2,4,5,6,7)