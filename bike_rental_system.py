class BikeShop:
    __stock = 0
    def __init__(self, stock):
        self.__stock = stock 
    def getTotalStock(self):
        return self.__stock
    def rentBikes(self, quantity):
        if quantity < 0:
            print("Enter valid quantity bikes ")
        elif quantity > self.__stock:
            print("Sorry, we don't have so many bikes")  
        else:
            self.__stock -= quantity
            print("Total price you have to pay", (quantity*100))
            print("Available stock of bikes :", self.__stock)          

obj = BikeShop(100)
while True:
    userChoice = int(input(''' 
       Select an option below :
       Press 1 (To display stock of bikes)
       Press 2 (To enter quantity of bikes, you want to rent)
       Press 3 (Exit)                                                            
    '''))  
    if userChoice == 1:
        print("Available stock of bikes", obj.getTotalStock())
    elif userChoice == 2:
        quantity = int(input('Enter quantity of bikes, you want to rent : '))
        obj.rentBikes(quantity)  
    else:
        break                