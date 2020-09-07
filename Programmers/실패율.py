def solution(N, stages):
    answer = []
    for i in range(1, N+1):
        up = down = 0
        for stage in stages:
            if stage >= i:
                down += 1
            if stage == i:
                up += 1
        if down == 0:
            answer.append((i, 0))
        else:
            answer.append((i, up/down))
    answer = sorted(answer, key=lambda y:y[1], reverse=True)
    result = []
    for i in range(len(answer)):
        result.append(answer[i][0])
    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))