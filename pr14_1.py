class Display:
    def printmsg(self,x,y):
        if type(x)==int:
            print("Integer Message=",x)
        else:
            print("Character Message=",x)
a=Display()
a.printmsg(50,'ABC')
a.printmsg('ABC',50)
