
# Project Euler Problem 2

import time
start=time.time()
t=[1]
n=2
while n<4000000:
    t.append(n)
    n= n+ t[-2]
sum=0
for k in t:
    if k%2==0:
        sum=k+sum
    else:
        continue
print(sum)
print('''<------- %f -------->''' %(time.time()-start))

