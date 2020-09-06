for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    pizza = [0] + list(map(int, input().split()))
    oven = []
    pos = N + 1

    while len(oven) > 1:
        num = oven.pop(0)
        pizza[num] //= 2
        if pizza[num]:
            oven.append(num)
        else:
            if pos <= M:
                oven.append(pos)
                pos += 1
    print(oven[0])