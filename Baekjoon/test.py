import time
start = time.time()
result = 0
f = open('input.txt', 'w')
data = ''
for i in range(1000):
    for j in range(10000):
        data += '0 '
    data += '\n'
f.write(data)
f.close()
print(time.time()-start)