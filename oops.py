class MyClass:
    __private_var = 10
    _protected_var = 20
    public_var = 30
    def __init__(self):
        print("Constructor initialization ...")
        # self.__value = 50
    def func(self):
        print("Hello Everyone ...")
    def __getSum(self, a, b):
        return a + b   
    def printSum(self, a, b):
        self.sum = self.__getSum(a, b) 
        print(self.sum)
    def multi(self):
        return self.__private_var * self._protected_var * self.public_var    

obj = MyClass()
obj.func()  
# output = obj.__getSum(10, 20) # private member method
obj.printSum(10, 20)
product = obj.multi() # public member method
# print(obj.__private_var) # private member variable
# print(obj._protected_var) # protected member variable
# print(obj.public_var) # public member variable
print(product)
# print(obj.__value)


    