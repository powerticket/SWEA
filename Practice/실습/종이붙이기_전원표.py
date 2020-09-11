memo = [0, 1, 3]
for t in range(1, 1+int(input())):
    n = int(input()) // 10
    for i in range(len(memo), n+1):
        memo.append(pow(2, i-1) + memo[i-2])
    print('#{} {}'.format(t, memo[n]))