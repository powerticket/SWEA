N = int(input())
roof = [0] * 1001
max_L = 0
max_H = 0
for _ in range(N):
    L, H = map(int, input().split())
    roof[L] = H
    if H > max_H:
        max_H = H
        max_L = L
sum_height = 0
cur_height = 0
for i in range(1, max_L+1):
    if roof[i] > cur_height:
        cur_height = roof[i]
    sum_height += cur_height
cur_height = 0
for i in range(1000, max_L, -1):
    if roof[i] > cur_height:
        cur_height = roof[i]
    sum_height += cur_height
print(sum_height)