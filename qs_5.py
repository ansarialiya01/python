from collections import deque

MAX_SIZE = 5
circular_queue = deque(maxlen = MAX_SIZE)
def isEmpty():
    return not circular_queue

def enqueue(item):
    if len(circular_queue)==MAX_SIZE:
        print("queue is full")
    else:
        circular_queue.append(item)

def dequeue():
    if isEmpty():
        print("queue is empty")
    else:
        circular_queue.popleft()

def peek():
    if isEmpty():
        print("queue is empty")
    else:
        print("Top element: ", circular_queue[0])

enqueue(69)
enqueue(87)
enqueue(99)
enqueue(34)

print(circular_queue)

dequeue()
print(circular_queue)

peek()