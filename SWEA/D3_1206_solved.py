for t in range(1, 11):
    N = int(input())
    L = list(map(int, input().split()))
    view = [0] * len(L)
    for i in range(2, len(L)-2):
        if L[i] > max(L[i-2:i] + L[i+1:i+3]):
            view[i] = L[i] - max(L[i-2:i] + L[i+1:i+3])
    print(f'#{t} {sum(view)}')
