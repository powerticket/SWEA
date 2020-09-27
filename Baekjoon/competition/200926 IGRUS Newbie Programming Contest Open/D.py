def find_comb(cur_sum, cur_comb):
    if cur_sum == Y:
        comb_list.append(cur_comb)
    elif cur_sum > Y:
        return
    find_comb(cur_sum+1, cur_comb+'1')
    find_comb(cur_sum+3, cur_comb+'3')
    find_comb(cur_sum+5, cur_comb+'5')


H, Y = map(int, input().split())
comb_list = []
find_comb(0, '')
max_profit = H
for comb in comb_list:
    profit = H
    for y in [int(year) for year in comb]:
        if y == 1:
            profit = int(profit*1.05)
        elif y == 3:
            profit = int(profit*1.2)
        elif y == 5:
            profit = int(profit*1.35)
    if profit > max_profit:
        max_profit = profit
print(max_profit)