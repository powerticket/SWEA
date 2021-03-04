import sys
sys.stdin = open('0304_2758.txt', 'r')

# 03/04
# 2758 로또

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    # n개까지 고를 수 있는 경우의 수를 담는 배열
    dp = [[i for i in range(m+1)]] + [[0] * (m + 1) for _ in range(n-1)]
    # 경우의 수는 왼쪽 배열 + 이전 단계 배열(해당 숫자의 절반인 배열)의 합
    for i in range(1, n):
        for j in range(1, m+1):
            if (1 << n - i - 1) * j <= m:
                dp[i][j] = dp[i][j-1] + dp[i-1][j//2]
    # 마지막 행, 마지막 열의 값이 정답
    print(dp[n-1][m])
