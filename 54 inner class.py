class student:
    def __init__(self, name,rollno):
        self.name = name
        self.rollno= rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand= "hp"
            self.ram= 8
            self.series= "i5"
        def show(self):
            print(self.brand,self.ram,self.series)

s1=student("praveen",14)
s2=student("shivappa",17)
s2.show()

