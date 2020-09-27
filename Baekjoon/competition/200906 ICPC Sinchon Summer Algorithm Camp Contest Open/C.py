N, H, T = map(int, input().split())
giants = [int(input()) for _ in range(N)]
tallest = 0
result = 1
giants.sort()
time = T
while giants:
    g = giants.pop()
    if g < H:
        break
    while g >= H:
        if time == 0:
            result = 0
            giants.clear()
            break
        g //= 2 if g != 1 else 1
        time -= 1
    if g > tallest:
        tallest = g

if result:
    print('YES')
    print(T-time)
else:
    print('NO')
    print(tallest)