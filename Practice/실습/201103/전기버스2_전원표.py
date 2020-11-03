def dfs(k, cur_battery, cur_charge):
    global min_charge
    if cur_charge >= min_charge:
        return
    if k == arr[0]:
        if cur_charge < min_charge:
            min_charge = cur_charge
        return
    if cur_battery - 1 >= 0:
        dfs(k+1, cur_battery-1, cur_charge)
    cur_battery = arr[k]
    cur_charge += 1
    dfs(k+1, cur_battery-1, cur_charge)


T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    min_charge = arr[0] - 1
    dfs(2, arr[1]-1, 0)
    print('#{} {}'.format(t, min_charge))
