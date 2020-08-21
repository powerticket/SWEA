N, M = map(int, input().split())
if N > 100 or not M in [1, 2, 3]:
    print("INPUT ERROR!")
else:
    if M == 1:
        for i in range(N):
            for j in range(i+1):
                print('*', end='')
            print()
    elif M == 2:
        for i in range(N):
            for j in range(N-i):
                print('*', end='')
            print()
    else:
        for i in range(N):
            print(' ' * (N-i-1), end='')
            print('*' * (2*i+1))