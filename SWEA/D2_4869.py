def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return pow(2, n-1) + paper(n-2)


for t in range(1, int(input())+1):
    print('#{} {}'.format(t, paper(int(input())//10)))