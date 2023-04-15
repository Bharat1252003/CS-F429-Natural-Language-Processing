import time
i = 0
since = time.time()
for j in range(100000):
    i+=1
print(time.time()-since)
