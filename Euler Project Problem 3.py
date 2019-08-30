
# Project Euler Problem 3

import time
start_time = time.time()
list=[]
n=600851475143
t=2
while n>1:
    if n%t==0:
        n=n/t
        list.append(t)
    else:
        t=t+1
print(sorted(list)[-1])

print("--- %f seconds ---" % (time.time() - start_time))

