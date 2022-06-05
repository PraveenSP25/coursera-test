class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a,*b):
        s=a
        for i in b:
            s=s+i
        return s
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)
s1=student(40,57)
print(s1.sum(3,7))
print(s1)