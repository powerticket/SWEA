def merge(left, right):
    result = []
    if left[-1] > right[-1]:
        global count
        count += 1
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif left:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
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
