import time
start = time.time()


def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-2) + fibo(n-1)


print(fibo(30))
print(time.time()-start)