Q = [0] * 100
front = rear = -1


def createQueue():
    pass


def enQueue(item):
    if isFull():
        print('Queue is full!')
        return
    global rear
    rear += 1
    Q[rear] = item


def deQueue():
    if isEmpty():
        print('Queue is empty!')
        return
    global front
    front += 1
    return Q[front]


def isEmpty():
    return front == rear


def isFull():
    return rear == len(Q)-1


def Qpeek():
    if isEmpty():
        print('Queue is empty!')
        return
    return Q[front+1]


enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())