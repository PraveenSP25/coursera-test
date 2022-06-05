class a:
    def __init__(self):  #### here it print only constructor the o/p is init of a
        print('init of a')

    def feature1(self):
        print("feature 1 print")

    def feature2(self):
        print("feature 2 print")
class b(a):  ### b(a)  over hera we inherits the value from a

    def __init__(self):#### we type constructor in class a and class b that time it print constructor 1st
        super().__init__()  ### we type super .init that time it print class a and class b constructor
        print("init of b")
    def feature3(self):
        print("feature 3 print")

    def feature4(self):
        print("feature 4 print")
b1=b()                                        ### only we call class b only we call class a and b at a time it print both constructor