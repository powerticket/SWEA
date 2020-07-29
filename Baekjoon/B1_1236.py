L = list(map(int, input().split()))
n, m = L[0:2]
d = dict()
need = max(n, m)
d = dict()
if n >= m:
    for row in range(n):
        castle = input().upper()
        need -= bool(castle.count("X"))
else:
    for row in range(n):
        castle = input().upper()
        for i in range(len(castle)):
            if castle[i] == "X":
                d[i] = 1
    need -= sum(d.values())
print(need)