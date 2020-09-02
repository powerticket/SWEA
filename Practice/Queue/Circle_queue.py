SIZE = 4
Q = [0] * SIZE
front = rear = 0


def enQueue(item):
    if isFull():
        print('Queue is full!')
        return
    global rear
    rear = (rear+1) % SIZE
    Q[rear] = item


def deQueue():
    if isEmpty():
        print('Queue is empty!')
        return
    global front
    front = (front+1) % SIZE
    return Q[front]


def isEmpty():
    return front == rear


def isFull():
    return front == (rear+1) % SIZE


def Qpeek():
    if isEmpty():
        print('Queue is empty!')
        return
    return Q[(front+1) % SIZE]


enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())