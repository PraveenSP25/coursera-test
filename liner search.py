#pos=-1   we use while loop #here we define global variable bcs of findind index no of list
def search(list, n):
    i = 0
    for i in range(len(list)): ## here while i< len(list)
        if list[i] == n:
           # globals()['pos']=i # here we define global variable

            return True
# in while loop we use increment i=i+1
    return False

list =  [2,3,4,5,6,7,8,21,54,32,76,89766,23,6234,3543,431,32,637343,42543254645,43,53,6546]
n =int(input("enter any number"))
if search(list, n):
    print("found",list.index(n)) ## "found",pos  over here we type
else:
    print('not found')