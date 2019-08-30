# Project Euler Problem 1
import time
start=time.time()
list_of_multiples=[]
k=1
while k<1000:
    if k%3==0 or k%5==0:
        list_of_multiples.append(k)
        k=k+1
    else:
        k=k+1
        continue
print(sum(list_of_multiples))
print('''<-------- %f seconds -------> ''' %(time.time()-start))
