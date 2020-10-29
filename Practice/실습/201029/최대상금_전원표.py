def swap(change):
    if change == 0:
        global max_price
        cur_price = int(''.join(price))
        if cur_price > max_price:
            max_price = cur_price
        return
    for i in range(len_price):
        for j in range(len_price):
            if i != j:
                price[i], price[j] = price[j], price[i]
                swap(change-1)
                price[i], price[j] = price[j], price[i]


T = int(input())
for t in range(1, T+1):
    price, change = input().split()
    price = list(price)
    change = int(change)
    len_price = len(price)
    if change >= len_price-1:
        for i in range(len_price):
            max_idx = i
            for j in range(i, len_price):
                if price[j] > price[max_idx]:
                    max_idx = j
                    change -= 1
            price[i], price[max_idx] = price[max_idx], price[i]
        if change % 2:
            for i in range(1, len_price):
                if price[i-1] == price[i]:
                    break
            else:
                price[-1], price[-2] = price[-2], price[-1]
        max_price = int(''.join(price))
    else:
        max_price = 0
        swap(change)
    print('#{} {}'.format(t, max_price))
