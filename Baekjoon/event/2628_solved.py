x, y = map(int, input().split())
N = int(input())
x_cut = [0, x]
y_cut = [0, y]
for _ in range(N):
    d, cut = map(int, input().split())
    if d:
        x_cut.append(cut)
    else:
        y_cut.append(cut)
x_max = 1
y_max = 1
x_cut.sort(reverse=True)
y_cut.sort(reverse=True)
len_x_cut = len(x_cut)
len_y_cut = len(y_cut)
for i in range(len_x_cut-1):
    diff = x_cut[i] - x_cut[i+1]
    if diff > x_max:
        x_max = diff
for i in range(len_y_cut-1):
    diff = y_cut[i] - y_cut[i+1]
    if diff > y_max:
        y_max = diff
print(x_max*y_max)