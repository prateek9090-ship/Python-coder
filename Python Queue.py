# Create an empty queue
queue = []

# Enqueue (add elements)
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue:", queue)

# Dequeue (remove element)
removed = queue.pop(0)
print("Dequeued element:", removed)

# Front element
print("Front element:", queue[0])

# Check if queue is empty
if len(queue) == 0:
    print("Queue is empty")
else:
    print("Queue is not empty")