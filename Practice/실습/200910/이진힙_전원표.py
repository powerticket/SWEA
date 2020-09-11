def heap_push(item):
    global heap_cnt
    heap_cnt += 1
    heap[heap_cnt] = item
    cur = heap_cnt
    parent = cur // 2
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent //= 2


for t in range(1, int(input())+1):
    N = int(input())
    heap_cnt = 0
    heap = [0] * (N+1)
    for h in map(int, input().split()):
        heap_push(h)
    result = 0
    while N > 1:
        N //= 2
        result += heap[N]
    print('#{} {}'.format(t, result))      