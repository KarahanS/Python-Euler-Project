
# Project Euler Problem 8

import time
start_time = time.time()

f=open("C:\Program Files\Python 3.7\Project Euler Problem 8 Number.txt")
a=f.readlines()


k=0
while k<len(a):
    a[k]=a[k].strip()
    k=k+1

a="".join(a)
number_list=list(a)

t={}
multiplelist=[]
i=0
while i<988:
    new_list=number_list[i:i+13]
    sayı="".join(new_list)
    i=i+1
    multiple=1
    for k in new_list:
        multiple=multiple*int(k)
    t[sayı]=multiple

a=sorted(t.values())
for l in t:
    if a[-1]==t[l]:
        print(l," --> multiplication of these numbers =",t[l])


print("--- %f seconds ---" % (time.time() - start_time))

