class computer:
    def __init__(self):
        self.name="praveen"
        self.age=23

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

c1=computer()
c1.age=25
c2=computer()

if c1.compare(c2):## here we do not mention any value in bracket age or name but self is help lin e number 5
    print("they are same")
else:
    print("not same")

print(c1.name)
print(c2.age)