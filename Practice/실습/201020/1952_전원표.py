def dfs(cur_month, cur_price):
    global result
    if cur_month > 11:
        if cur_price < result:
            result = cur_price
        return
    elif cur_price >= result:
        return    
    dfs(cur_month+3, cur_price+price[2])
    dfs(cur_month+1, cur_price+price[1])
    dfs(cur_month+1, cur_price+plan[cur_month]*price[0])


T = int(input())
for t in range(1, T+1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    result = price[3]
    dfs(0, 0)
    print('#{} {}'.format(t, result))
