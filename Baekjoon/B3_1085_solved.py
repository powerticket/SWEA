x, y, w, h = tuple(map(int, input().split()))
print(min(x, y, w-x, h-y))