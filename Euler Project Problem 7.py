
# Project Euler Problem 7

import math
import time
start_time = time.time()
list=[2]
a=1
while len(list)<10001:
    a=a+2
    t = 2
    while t<=round(math.sqrt(a)):
        k=True
        if a%t==0 and t!=a:
            k=False
            break
        t=t+1
    if k==True:
        list.append(a)


print(list[-1])
print("--- %f seconds ---" % (time.time() - start_time))

