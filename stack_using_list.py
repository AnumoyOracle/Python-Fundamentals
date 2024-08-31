stack = []

while True:
    print('''
       Enter 
          1 -> Push an element inside stack
          2 -> Pop an element from stack
          3 -> Display the last element 
          4 -> Display whole stack
          5 -> Exit
          ''')
    option = int(input("Enter suitable option : "))
    if option == 1:
        element = int(input('Enter element -> '))
        stack.append(element)
        print(stack)
    elif option == 2:
        stack.pop()
        print(stack)
    elif option == 3:
        element = stack[-1]
        print("Popped element : ", element)
    elif option == 4:
        print("Displayed stack : ")
        print(stack)
    elif option == 5:
        break;  
    else:
        print("Invalid operation ...")
        break;  
