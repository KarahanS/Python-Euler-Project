
# Project Euler Problem 4

import time
start_time = time.time()
i=range(100,1000)
l=[]
for k in i:
    for t in i:
        multiple=k*t
        end=str(multiple)
        reverse=end[::-1]
        if end==reverse:
            l.append(int(end))
        else:
            continue
print(sorted(l)[-1])

print("--- %f seconds ---" % (time.time() - start_time))

