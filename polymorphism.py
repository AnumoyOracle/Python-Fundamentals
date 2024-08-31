class A:
    def getArea(self, a = None, b = None):
        if a != None and b != None :
            return a * b
        elif a != None:
            return a * a 
        else:
            return 0
    def func(self):
        print("A class function ...")    

class B(A):
    def func(self):
        print("B class function ...")

obj = B()
obj.func() # method overriding
print(obj.getArea(10, 20)) # method overloading
print(obj.getArea(10))
print(obj.getArea())