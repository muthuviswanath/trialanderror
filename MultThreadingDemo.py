#Thread Module
#Threading Module

import _thread
import time
# _thread.start_new_thread(functionname, args, [, kwargs])

def find_square(numlist):
    print ("Square of the numbers in the list: ")
    for n in numlist:
        time.sleep(5)
        print(f"Square of {n} is : {n*n}")


def find_power(numlist, exp):
    print ("Power of the numbers in the list: ")
    for n in numlist:
        time.sleep(5)
        print(f"Power of {n} is : {n**exp}")

tstart = time.time()
_thread.start_new_thread(find_square, (2,3,5,7,11))
print(f"Time taken: {time.time()-tstart}")