class Degree:
    def getDegree(self):
         print("I got Diploma degree")
class Undergraduate(Degree):
    def getDegree(self):
         print("I got Undergraduate degree")
class Postgraduate(Degree):
    def getDegree(self):
         print("I got Postgraduate degree")
d=Degree()
u=Undergraduate()
p=Postgraduate()
d.getDegree()
u.getDegree()
p.getDegree()
