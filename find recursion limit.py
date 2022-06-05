import sys
sys.setrecursionlimit(2000)
print((sys.getrecursionlimit()))
i=0
def g():
    global i
    i=i+1
    print("hello",i)
    g()
g()