class car:
    wheel=4     #class varibale or static
    def __init__(self):
        self.milg=10         ### instance variable
        self.compny="bmw"
c1=car()
c2=car()
c2.milg=8

car.wheel=5   ## we update class variable

print(c1.compny, c1.milg, c1.wheel)
print(c2.compny, c2.milg, c2.wheel)