# sum the first 9 numbers
import time
start_time = time.time()
s = 0
for i in range(0, 10**7):
    s += i
print(s)
print(f"it took {time.time()-start_time}")

n = 0
s = 0
start_time = time.time()
while n < 10**7:
    s += n
    n += 1
print(s)
print(f"it took {time.time()-start_time}")
