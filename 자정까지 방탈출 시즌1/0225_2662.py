import sys
sys.stdin = open('0225_2662.txt', 'r')

# 02/25
# 2662 기업투자

N, M = map(int, input().split())
invest = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]
print(invest)
max_profit = -1
max_index = -1
for i in range(N+1):
    profit = invest[i][1] + invest[N-i][2]
    if profit > max_profit:
        max_profit = profit
        max_index = i
        
print(max_profit)
print(max_index, N-max_index)
