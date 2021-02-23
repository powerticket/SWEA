# import sys
# sys.stdin = open('0223_1843.txt', 'r')

# 02/23
# 1843 방정식

N = int(input())
A = B = C = 0
# check A
for i in range(1, N//2+1):
    A += N - 2 * i
print(A)

# check B
div = set()
div_check = [0] * (N+1)
for i in range(1, int(N ** 0.5 + 1)):
    if not N % i:
        div.add(i)
        div.add(N//i)
        div_check[i] = 1
        div_check[N//i] = 1
div = list(div)
len_div = len(div)
for i in range(len_div):
    for j in range(i, len_div):        
        if div[i]+div[j] <= N and div_check[div[i]+div[j]]:
            B += 1
print(B)

# check C
# prime check
prime_check = [0] * (N+1)
prime = []
for i in range(2, N+1):
    if not prime_check[i]:
        for j in range(i, N+1, i):
            prime_check[j] = -1
        prime_check[i] = 1
        prime.append(i)
for p in prime:
    if p + 2 <= N and prime_check[p + 2] == 1:
        C += 1
print(C)
