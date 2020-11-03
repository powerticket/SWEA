def merge(left, right):
    len_left = len(left)
    len_right = len(right)
    result = [0] * (len_left+len_right)
    if left[-1] > right[-1]:
        global count
        count += 1
    l = r = 0
    i = 0
    while l < len_left or r < len_right:
        if l < len_left and r < len_right:
            if left[l] <= right[r]:
                result[i] = left[l]
                l += 1
            else:
                result[i] = right[r]
                r += 1
        elif l < len_left:
                result[i] = left[l]
                l += 1
        else:
            result[i] = right[r]
            r += 1
        i += 1
    return result


def merge_sort(arr):
    len_arr = len(arr)
    if len_arr == 1:
        return arr
    mid = len_arr // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    mid = N // 2
    count = 0
    result = merge_sort(arr)
    print('#{} {} {}'.format(t, result[mid], count))
