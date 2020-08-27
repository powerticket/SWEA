def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append(arr[i])
        elif arr[i] == ')':
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    return True


stack = []
arr = "()()((()))"
print(check(arr))