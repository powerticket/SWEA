def subset(idx, cur_arr):
    if idx == len(arr):
        print(cur_arr)
        return
    subset(idx+1, cur_arr)
    cur_arr += ' ' + str(arr[idx])
    subset(idx+1, cur_arr)


arr = [1, 2, 3, 4, 5]
subset(0, '')
