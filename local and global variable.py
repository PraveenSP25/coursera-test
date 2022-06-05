a= 10
def sum():
    # global a-----if we update global then type global
    a=15
    print("inside variable:", a)
sum()
print("outside variable:",a)