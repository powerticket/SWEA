def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i <= j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


arr = [10, 7, 82, 2]
n = len(arr)
quick_sort(arr, 0, n-1)
print(arr)