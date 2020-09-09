import heapq


# 최소힙만 지원 (heapq)
heap = [7, 2, 5, 3, 4, 6] # list
print(*heap)
heapq.heapify(heap)
print(*heap)
heapq.heappush(heap, 1)
print(*heap)
while heap:
    print(heapq.heappop(heap), end=' ')


temp = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, (-temp[i], temp[i]))
print(heap2)