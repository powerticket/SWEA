def turn(gear, direction):
    if direction == 1:
        return [gear[-1]] + gear[0:-1]
    elif direction == -1:
        return gear[1:] + [gear[0]]
    else:
        return gear
 
 
T = int(input())
for t in range(1, T+1):
    K = int(input())
    gears = [input().split() for _ in range(4)]
    control = [list(map(int, input().split())) for _ in range(K)]
    for start, direction in control:
        turn_or_not = [0] * 4
        index = start - 1
        turn_or_not[index] = direction
        front_index = index + 1
        front_direction = -direction
        while front_index < 4:
            if gears[front_index][6] != gears[front_index-1][2]:
                turn_or_not[front_index] = front_direction
                front_direction *= -1
                front_index += 1
                continue
            break 
        back_index = index - 1
        back_direction = -direction
        while back_index >= 0:
            if gears[back_index][2] != gears[back_index+1][6]:
                turn_or_not[back_index] = back_direction
                back_direction *= -1
                back_index -= 1
                continue
            break
        for i in range(4):
            gears[i] = turn(gears[i], turn_or_not[i])
    score = 0
    for i in range(4):
        if gears[i][0] == '1':
            score += 1 << i
    print('#{} {}'.format(t, score))
