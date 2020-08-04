T = int(input())
for t in range(1, T+1):
    N = int(input())
    snail = dict()
    x = y = 0
    xstart, ystart = 0, 1
    xend = yend = N-1
    distance = 1
    direction = 1
    while 1:
        if distance == N**2+1:
            break
        try:
            snail[x, y] += 0
        except:
            snail[x, y] = distance
            distance += 1
        if direction == 1:
            if x < xend:
                x += 1
            else:
                xend -= 1
                direction = direction + 1 if direction < 4 else 1
        elif direction == 2:
            if y < yend:
                y += 1
            else:
                yend -= 1
                direction = direction + 1 if direction < 4 else 1
        elif direction == 3:
            if x > xstart:
                x -= 1
            else:
                xstart += 1
                direction = direction + 1 if direction < 4 else 1
        elif direction == 4:
            if y > ystart:
                y -= 1
            else:
                ystart += 1
                direction = direction + 1 if direction < 4 else 1
    print('#{}'.format(t))
    for i in range(N):
        for j in range(N):
            print(snail[j, i], end=' ')
        print()
