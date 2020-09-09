def is_empty():
    return lastidx == 0


def is_full():
    return lastidx == size


def add(n):
    global lastidx
    if is_full():
        print('Full!')
        return
    lastidx += 1
    tree[lastidx] = n

# VLR 전위순회
def preorder(idx):
    if idx <= lastidx:
        print(tree[idx], end=' ')
        preorder(2*idx)
        preorder(2*idx+1)

# LVR 중위순회
def inorder(idx):
    if idx <= lastidx:
        inorder(2*idx)
        print(tree[idx], end=' ')
        inorder(2*idx+1)

# LRV 후위순회
def lastorder(idx):
    if idx <= lastidx:
        lastorder(2*idx)
        lastorder(2*idx+1)
        print(tree[idx], end=' ')


size = 15
tree = [0] * (size+1)
lastidx = 0

for i in range(0, 10):
    print(chr(i+65))
    add(chr(i+65))
print(tree)
preorder(1)  # 루트부터 전위순회
print()
inorder(1)   # 루트부터 중위순회
print()
lastorder(1) # 루트부터 후위순회
print()