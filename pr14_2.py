class Area:
    def printArea(self,x,y=None):
         if y is not None:
             print("Area of Rectangle=",x*y)
         else:
             print("Area of Square=",x*x)
a=Area()
a.printArea(10)
a.printArea(10,20)
