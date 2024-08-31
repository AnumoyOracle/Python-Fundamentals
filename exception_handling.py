# Different types of logical errors (exceptions) are :

# 1. ZeroDivisionError
# 2. NameError
# 3. TypeError
# 4. ValueError
# 5. IndexError
# 6. ImportError
# 7. ModuleNotFoundError
# 8. KeyError

try:
    # import cals
    value = 10/0
    # list = [1, 2, 3, 4]
    # print(list[4])
    # print('10' + 10)
    # user_input = int(input('Enter value : ')) 
    # from calcmodule import diva  
    # dict = {
    #     'key1' : 'value1',
    #     'key2' : 'value2',
    #     'key3' : 'value3'
    # }
    # print(dict["key4"])
except ZeroDivisionError:
    print("You can't divide a number with zero")
except IndexError:
    print("You can't access out of bound index in an array")
except TypeError:
    print("You can't concatenate two different types of datatypes")
except ValueError:
    print("You can't treat a string as integer") 
except ModuleNotFoundError:
    print("Module can't be found")
except ImportError:
    print("Module hasn't imported correctly")  
except KeyError:
    print("You can't access invalid key")          
except Exception as e:
    print("General purpose exception")       
# else:
#     print("General purpose exception")
finally:
    print("Execution after every attempt")                        

