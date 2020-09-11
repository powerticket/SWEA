for t in range(1, int(input())+1):
    N = int(input())
    scores = list(map(int, input().split()))
    MAX_SCORE = sum(scores)
    arr = [1] + [0] * MAX_SCORE
    result = 1
    for score in scores:
        for i in range(MAX_SCORE, -1, -1):
            if i >= score and not arr[i]:
                if arr[i-score]:
                    arr[i] = 1
                    result += 1
    print('#{} {}'.format(t, result))
