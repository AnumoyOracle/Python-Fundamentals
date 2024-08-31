class A:
    def __init__(self):
        print("A class constructor ...")
    def printA(self):
        print("A class function ...")

class D:
    def __init__(self):
        print("D class constructor ...")
    def printD(self):
        print("D class function ...")        

class B(A):
    def __init__(self):
        super().__init__() # invoke parent class constrcutor explicitly
        print("B class constructor ...")
    def printB(self):
        super().printA() # invoke parent class member function
        print("B class function ...") 

class C(B):
    def __init__(self):
        super().__init__() # invoke parent class constrcutor explicitly
        print("C class constructor ...")
    def printC(self):
        super().printB() # invoke parent class member function
        print("C class function ...")   

class E(A,D):
    def __init__(self):
        super().__init__() # invoke parent class constructor                        
        D.__init__(self) # explicitly call D class constructor
    def printE(self):
        super().printA()
        super().printD()

# obj = C()
# obj.printC() 

obj2 = E()
obj2.printE()