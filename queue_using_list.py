queue = []

while True:
    print('''
       Enter 
          1 -> Push an element inside queue
          2 -> Pop front element from queue
          3 -> Display the front element 
          4 -> Display whole queue
          5 -> Exit
          ''')
    option = int(input("Enter suitable option : "))
    if option == 1:
        element = int(input('Enter element -> '))
        queue.append(element)
        print(queue)
    elif option == 2:
        queue.pop(0)
        print(queue)
    elif option == 3:
        element = queue[0]
        print("Popped element : ", element)
    elif option == 4:
        print("Displayed queue : ")
        print(queue)
    elif option == 5:
        break;  
    else:
        print("Invalid operation ...")
        break;  
