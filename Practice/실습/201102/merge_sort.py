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
    if len(arr) == 1:
        return arr
    left = []
    right = []
    mid = len(arr) // 2
    for i in range(len(arr)):
        if i < mid:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return merge(merge_sort(left), merge_sort(right))


arr = [69, 10, 30, 2, 16, 8, 31, 22]
arr_result = merge_sort(arr)
print(arr_result)
