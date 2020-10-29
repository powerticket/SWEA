T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    result = 0
    container.sort(reverse=True)
    truck.sort(reverse=True)
    while truck:
        t = truck.pop(0)
        while container:
            c = container.pop(0)
            if t >= c:
                result += c
                break
    print('#{} {}'.format(tc, result))
