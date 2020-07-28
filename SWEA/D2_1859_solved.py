T = int(input())

for t in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    print(f'#{t} ', end='')
    profit = 0
    max_price = L[-1]
    for n in range((len(L))-1, -1, -1):
        if L[n] <= max_price:
            profit += max_price - L[n]
        else:
            max_price = L[n]
    print(profit)


# Runtime error
# T = int(input())

# for t in range(1, T+1):
#     N = int(input())
#     L = list(map(int, input().split()))
#     print(f'#{t} ', end='')
#     profit = 0
#     for n in range(N):
#         if L[n] < max(L[n:N]):
#             profit += max(L[n:N]) - L[n]
#     print(profit)