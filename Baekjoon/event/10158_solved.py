w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
dw = p + t
dh = q + t
if (dw // w) % 2:
    x = w - (dw % w)
else:
    x = dw % w
if (dh // h) % 2:
    y = h - (dh % h)
else:
    y = dh % h
print(x, y)