class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("ip config :", self.cpu, self.ram)


com1=computer("amd",8)
com2=computer("intel",16)

com1.config()
com2.config()