L = input().split()

x = L[0]
y = L[1]

def reverse(L):
    return L[::-1]

z = int(reverse(x)) + int(reverse(y))

print(int(reverse(str(z))))