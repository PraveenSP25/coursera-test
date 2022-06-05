class student:
    school = 'bangalore institute of technology'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3/3)
    def get_m1(self):#### fetch the value of m1 using accesoor method instance method or we can use s1.m1 in last printing statement
        return self.m1
    def set_m1(self):### modifyied the value instance method
        self.m1 = 15

    @classmethod
    def getschool_name(prv):  ### we use class variable to get school name
        return prv.school
    @staticmethod
    def info():  ### in static method we dont use any variable and object like self
        print("this is one of the top 10 college in bangalore")


s1 = student(25,23,46)
s2 = student(34,65,12)
print(s1.m1)
print(s1.avg())
print(s1.get_m1())
print(s1.set_m1())
print(student.getschool_name())
student.info()
