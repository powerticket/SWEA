# Python Style

def push(item):
    stack.append(item)


def pop():
    if len(stack) == 0:
        print("Stack is empty!")
        return
    else:
        return stack.pop()


stack = []

push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())