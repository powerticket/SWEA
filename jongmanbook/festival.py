"""
2
6 3 
1 2 3 1 2 3 
6 2 
1 2 3 1 2 3
"""

T = int(input())
for t in range(1, T+1):
    N, L = map(int, input().split())
    price = list(map(int, input().split()))
    min_price = cur_price = sum(price[:L])
    for i in range(L, N):
        cur_price += price[i]
        cur_price -= price[i-L]
        if cur_price < min_price:
            min_price = cur_price
    print(min_price/L)
