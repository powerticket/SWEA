N = int(input())
arr = list(map(int, input().split()))
len_arr = len(arr)
max_up = 1
max_down = 1
cur_up = 1
cur_down = 1
for i in range(len_arr-1):
    if arr[i] <= arr[i+1]:
        cur_up += 1
        if cur_up > max_up:
            max_up = cur_up
    else:
        cur_up = 1
    if arr[i] >= arr[i+1]:
        cur_down += 1
        if cur_down > max_down:
            max_down = cur_down
    else:
        cur_down = 1
print(max(max_up, max_down))