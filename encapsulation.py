# Python doesn't support traditional method overloading (a, b=5, c=10)

class Student:
    __name = ""
    __dept = ""
    def __init__(self, name = "", dept = ""):
        self.__name = name
        self.__dept = dept
    def getName(self):
        return self.__name 
    def getDept(self):
        return self.__dept
    def setName(self, name):
        self.__name = name
    def setDept(self, dept):
        self.__dept = dept    
    def printDetails(self):
        print("Name : ", self.__name, ",", "Department : ", self.__dept)    

student = Student("Anumoy Nandy", "Fusion Shared Ops")
student.printDetails()

student2 = Student()
student2.setName("Mohit Sharma")
student2.setDept("Saas Production")
student2.printDetails()  


# print(student.getDept())
    