def paper(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    return paper(n-1) + 2*paper(n-2)


for t in range(int(input())):
    N = int(input()) // 10
    print(paper(N))