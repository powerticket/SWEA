import time
import sys
sys.stdin = open('input.txt', 'r')

start = time.time()

L = [list(map(int, sys.stdin.readline().split())) for _ in ' ' * 1000]
# result = 0
# for i in range(1000):
#     for j in range(10000):
#         if L[i][j]:
#             result = 1
#             break
#     if result:
#         break
# print(result)


# for i in range(1000):
#     if 1 in L[i]:
#         print(1)
#         break
# print(not all(map(all, L)))
print(time.time()-start)