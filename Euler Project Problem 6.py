
# Project Euler Problem 6

import time
start_time = time.time()
t=range(1,101)
sum_of_the_squares=0
for i in t:
    sum_of_the_squares+=i**2
sum=0
for i in t:
    sum+=i
square_of_the_sum=sum**2
print(square_of_the_sum-sum_of_the_squares)

print("--- %f seconds ---" % (time.time() - start_time))

