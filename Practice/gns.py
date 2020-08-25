import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, int(input())+1):
    new_number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    N = input().split()
    L = input().split()
    for i in range(len(L)):
        L[i] = new_number.index(L[i])
    L.sort()
    for i in range(len(L)):
        L[i] = new_number[L[i]]
    print('#{}'.format(t))
    print(' '.join(L))