
# Project Euler Problem 5     -- Should be updated --

import time
start_time = time.time()
l={}
for number in range(1,21):
    n = number
    t = 2
    k=1
    m=0
    while n > 1:
        if n % t == 0:
            n = n / t
            if t in l and k==1:
                m=m+1
                if m>l[t]:
                    l[t]=m
            else:
                l[t]=k
                k=k+1
                m=0


        else:
            t = t + 1
            k=1
            m=0
a=1
for k in l:
    m=k**l[k]
    a=m*a

print(a)


print("--- %f seconds ---" % (time.time() - start_time))

