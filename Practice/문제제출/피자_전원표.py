for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    circle_q = []
    out = []
    i = 0
    idx = 0
    for _ in range(N):
        i += 1
        circle_q.append([C.pop(0), i])
    while 1:
        circle_q[idx][0] //= 2
        if circle_q[idx][0] == 0:
            out.append(circle_q[idx][1])
            if C:
                i += 1
                circle_q[idx] = [C.pop(0), i]
            else:
                circle_q[idx] = [100, 0]
        idx = (idx + 1) % N
        if len(out) == M:
            break

    print('#{} {}'.format(t, out[-1]))
