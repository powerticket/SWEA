import heapq


temp = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, (-temp[i], temp[i]))
print(heap2)
print(heapq.heappop(heap2)[1])
print(heapq.heappop(heap2)[1])
print(heapq.heappop(heap2)[1])
print(heapq.heappop(heap2)[1])
print(heapq.heappop(heap2)[1])
print(heapq.heappop(heap2)[1])