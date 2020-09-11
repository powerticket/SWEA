for t in range(1, int(input())+1):
    N = int(input())
    T = [0] * (N+1)

    cnt = 0


    def inorder(v):
        global cnt
        if v > N:
            return
        inorder(v*2)
        cnt += 1
        T[v] = cnt
        inorder(v*2+1)


    inorder(1)
    print(T[1], T[N//2])