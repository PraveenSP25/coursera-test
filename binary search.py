pos=-1   #we use while loop #here we define global variable bcs of findind index no of list
def search(list, n):
    l = 0
    u=len(list)-1
    while l<=n: ## here while i< len(list)
        mid=(l+u) // 2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
list = [2,3,4,5,6,7,8,21,54,32,76]
n =int(input("enter any number"))
if search(list, n):
    print("found",pos) ## "found",pos  over here we type
else:
    print('not found')