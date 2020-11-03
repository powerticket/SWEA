def permutation(k, cur_distance, x, y):
    global min_distance
    if cur_distance >= min_distance:
        return
    if k == N:
        cur_distance += abs(x - home_x) + abs(y - home_y)
        if cur_distance < min_distance:
            min_distance = cur_distance
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            next_x, next_y = client[2*i], client[2*i+1]
            distance = abs(next_x - x) + abs(next_y - y)
            cur_distance += distance
            permutation(k+1, cur_distance, next_x, next_y)
            cur_distance -= distance
            visited[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    office_x, office_y = arr[:2]
    home_x, home_y = arr[2:4]
    client = arr[4:]
    min_distance = 0xffffffff
    visited = [0] * N
    permutation(0, 0, office_x, office_y)
    print('#{} {}'.format(t, min_distance))
