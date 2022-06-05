class a:
    def feature1(self):
        print("feature 1 print")

    def feature2(self):
        print("feature 2 print")
class b(a):  ### b(a)  over hera we inherits the value from a
    def feature3(self):
        print("feature 3 print")

    def feature4(self):
        print("feature 4 print")
a1=a()
a1.feature1()
a1.feature2()
a=b()
a.feature1()#### class b is inherits the value of a ..it shows feature 1 and 2 and 3 and 4