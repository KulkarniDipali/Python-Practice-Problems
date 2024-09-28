class Employee: 
    __id=0 
    __name="" 
    __department="" 
    __salary=0
    def setData(self): 
        self.__id=int(input("Enter Id:"))
        self.__name = input("Enter Name:")
        self.__department = input("Enter Department:")
        self.__salary =int(input("Enter Salary:"))
    def showData(self):
        print("*******Employee details******")
        print("Id:",self.__id) 
        print("Name:", self.__name) 
        print("Department:", self.__department) 
        print("Salary:", self.__salary) 
 
emp=Employee() 
emp.setData()
emp.showData() 

