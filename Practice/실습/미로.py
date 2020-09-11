dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def DFS(start_x, start_y):

    result = 0

    if arr[start_x][start_y] == 3:
        result = 1
        return result

    visited.append((start_x, start_y))

    for k in range(4):
        New_X = start_x + dx[k]
        New_Y = start_y + dy[k]
        if 0> New_X or New_X>=N or 0> New_Y or New_Y>=N: continue
        if (New_X, New_Y) in visited: continue
        if arr[New_X][New_Y] == 1: continue
        if DFS(New_X, New_Y) == 1:
            result = 1
            return result
    return result


T=int(input())
for t in range(1,T+1):
    N=int(input())
    arr=[list(map(int,(input()))) for _ in range(N)]
    # for ar in arr:
    #     print(ar)

    for x in range(N):
        for y in range(N):
            if arr[x][y] == 2:
                start_x = x
                start_y = y

    visited = []
    result = DFS(start_x, start_y)

    print("#{} {}".format(t, result))