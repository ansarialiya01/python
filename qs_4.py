stack = []
def isEmpty():
    if len(stack)==0:
        print("stack is empty")
        return
    else:
        print("stack is not empty", stack)

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        print("empty")
    else:
        print("pop element is", stack.pop())

def peek():
    if len(stack)==0:
        print("Empty")
    else:
        print("top element:", stack[-1])

def display():
    if len(stack)==0:
        print("Empty")
    else:
        print(stack)


if __name__=="__main__":
    push(34)
    push(3)
    push(88)
    push(56)
    push(3)
    push(79)
    display()

    pop()
    display()

    peek()

    isEmpty()