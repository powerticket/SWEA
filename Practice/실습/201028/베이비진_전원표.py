def check(arr):
    count = [0] * 10
    for a in arr:
        count[a] += 1
    straight = 0
    for c in count:
        if c > 2:
            return 1
        if c:
            straight += 1
        else:
            straight = 0
        if straight > 2:
            return 1


T = int(input())
for t in range(1, T+1):
    result = 0
    arr = list(map(int, input().split()))
    p1 = []
    p2 = []
    for _ in range(6):
        p1.append(arr.pop(0))
        p2.append(arr.pop(0))
        p1_check = check(p1)
        p2_check = check(p2)
        if p1_check:
            result = 1
            break
        elif p2_check:
            result = 2
            break
    print('#{} {}'.format(t, result))
