#Python program that calculates the time taken to execute a simple loop
import time
s=0
a=time.perf_counter_ns()
i=1
while i<=10 :
    s=s+1
    i=i+1
b=time.perf_counter_ns()

print("Total time ",(b-a))
