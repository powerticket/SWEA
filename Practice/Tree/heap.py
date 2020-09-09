def heap_push(item):
    global heap_cnt
    heap_cnt += 1
    heap[heap_cnt] = item

    cur = heap_cnt
    parent = cur // 2
    # 루트가 아니고, if 부모노드값 > 자식노드값 -> swap
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2


def heap_pop():
    global heap_cnt
    return_value = heap[1]
    heap[1] = heap[heap_cnt]
    heap[heap_cnt] = 0
    heap_cnt -= 1

    parent = 1
    child = parent * 2
    if child + 1 <= heap_cnt: # 오른쪽 자식이 존재
        if heap[child] > heap[child+1]:
            child += 1
    # 자식노드가 존재하고, if 부모노드 > 자식노드 -> swap
    while child <= heap_cnt and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heap_cnt: # 오른쪽 자식이 존재
            if heap[child] > heap[child+1]:
                child += 1
    return return_value


# min heap
heap_cnt = 0
temp = [7, 2, 5, 3, 4, 6]
N = len(temp)
heap = [0] * (N+1)
for i in range(N):
    heap_push(temp[i])
print(heap_pop(), end=' ')
print(heap_pop(), end=' ')
print(heap_pop(), end=' ')
print(heap_pop(), end=' ')
print(heap_pop(), end=' ')
print(heap_pop(), end=' ')
