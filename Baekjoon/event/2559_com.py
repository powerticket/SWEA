N, K = map(int, input().split())
temp = list(map(int, input().split()))
max_sum_temp = 0
for i in range(K):
    max_sum_temp += temp[i]
cur_sum_temp = max_sum_temp
for i in range(K, N):
    cur_sum_temp += temp[i]
    cur_sum_temp -= temp[i-K]
    if cur_sum_temp > max_sum_temp:
        max_sum_temp  = cur_sum_temp
print(max_sum_temp)