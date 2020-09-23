N = int(input())
switch = [0] + list(map(int, input().split()))
for _ in range(int(input())):
    gender, number = map(int, input().split())
    if gender == 1:
        for i in range(number, N+1, number):
            switch[i] = int(not switch[i])
    else:
        switch[number] = int(not switch[number])
        left = number - 1
        right = number + 1
        while left > 0 and right < N+1 and switch[left] == switch[right]:
            switch[left] = int(not switch[left])
            switch[right] = int(not switch[right])
            left -= 1
            right += 1
for i in range(1, N, 20):
    print(*switch[i:i+20])