'''
import time 
x = int(input("How many gigs?"))
for i in range(x+1):
    print("Iteration",i)
    a = []
    a = [0]*(i*2**27)
    time.sleep(5)
time.sleep(5)
print("done")
'''
import numpy as np
for i in range(100):
    print(np.sqrt((i+15)**2+15**2)-i, i)


