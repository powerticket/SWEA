T = int(input())

for t in range(1, T+1):
    L = list(map(int, input().split()))
    result = []
    for i in range(len(L)):
        for j in range(len(L)):
            for k in range(len(L)):
                if i != j and j != k and k != i:
                    result += [L[i]+L[j]+L[k]]
    result.sort()
    result = result[::-1]
    fifth = 1
    order = 0
    for i in range(1, len(result)):
        if result[order] != result[i]:
            order = i
            fifth += 1
            if fifth == 5:
                print('#{} {}'.format(t, result[i]))
                break
    else:
        print('#{} {}'.format(t, result[-1]))
