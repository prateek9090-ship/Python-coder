# Create an empty stack
stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

# Pop element
removed = stack.pop()
print("Popped element:", removed)

# Peek (top element)
print("Top element:", stack[-1])

# Check if stack is empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")