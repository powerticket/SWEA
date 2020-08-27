# C Language Style

def push(item):
    global top
    if top > 99:
        print("Stack is full!")
        return
    else:
        top += 1
        stack[top] = item


def pop():
    global top
    if top < 0:
        print("Stack is empty!")
        return
    else:
        result = stack[top]
        top -= 1
    return result


stack = [0] * 100
top = -1

push(1)
push(2)
push(3)
print(pop())
print(pop())
print(pop())