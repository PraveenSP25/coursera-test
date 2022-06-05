class pycharm:
    def exicute(self):
        print("running")
        print("compiling")
class myeditor:
    def exicute(self):
        print("spell check")
        print("running")
        print("compiling")

class laptop:
    def code(self, ide):
        ide.exicute()
ide=myeditor()
lap1=laptop()
lap1.code(ide)

