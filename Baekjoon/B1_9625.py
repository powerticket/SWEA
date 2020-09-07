da = [0] * 46
db = [0] * 46
da[0] = 1
N = int(input())
for i in range(1, N+1):
    da[i] = db[i-1]
    db[i] = da[i-1] + db[i-1]

print(da[N], db[N])