def merge(left, right):
    result = []
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
    merge_left = merge_sort(left)
    merge_right = merge_sort(right)
    return merge(merge_left, merge_right)


arr = [69, 10, 30, 2, 16, 8, 31, 22]
arr_result = merge_sort(arr)
print(arr_result)
