from collections import deque

stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

print(stack.pop())
print(stack.pop())

print(stack)