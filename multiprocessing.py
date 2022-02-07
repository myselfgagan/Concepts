from multiprocessing import Process
import numbers
import os
from time import time
from unittest import result

def square_num():
    for i in range(100):
        i*i

if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    # create processes
    for i in range(num_processes):
        p = Process(target = square_num)
        processes.append(p)
        
    # start
    for p in processes:
        p.start()
        
    # join
    for p in processes:
        p.join()
        
    print("end main")





# sharing memory between processes
from multiprocessing import Process, Value, Array, Lock
import time

def add100(num, lock):
    for i in range(100):
        time.sleep(0.01)     # race condition may occur here so we use lock 
        lock.acquire() 
        num.value += 1
        lock.release()
        
        # another way to use lock
        # with lock:
        #     num.value += 1

if __name__ == "__main__":
    
    lock = Lock()
    shared_number = Value("i", 0)
    print("Number at beginning is", shared_number.value)
    
    p1 = Process(target=add100,args=(shared_number,))
    p2 = Process(target=add100,args=(shared_number,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("number at the end is ", shared_number.value)
    
    
    

# sharing with array
from multiprocessing import Process, Value, Array, Lock
import time

def add100(nums, lock):
    for i in range(100):
        time.sleep(0.01)     # race condition may occur here so we use lock 
        
        lock.acquire() 
        for i in range(len(nums)):
            nums[i] += 1
        lock.release()
        
        # another way to use lock
        # with lock:
        #     for i in range(len(nums)):
        #     nums[i] += 1

if __name__ == "__main__":
    
    lock = Lock()
    shared_array = Array("d", [0.0, 100.0, 200.0])
    print("Array at beginning is", shared_array[:])
    
    p1 = Process(target=add100,args=(shared_array,))
    p2 = Process(target=add100,args=(shared_array,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("Array at end is", shared_array[:])
    
    
    
# Using queues
from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
import time

def square(nums, queue):
    for i in nums:
        queue.put(i*i)
        
def negative(nums, queue):
    for i in nums:
        queue.put(-1*i)

if __name__ == "__main__":
    
    numbers = range(1,6)
    q = Queue()
    
    p1 = Process(target = square, args=(numbers,q))
    p2 = Process(target = negative, args=(numbers,q))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    while not q.empty():
        print(q.get())
        
        
        
        

# process pool
from multiprocessing import Pool

def cube(nums):
    return nums*nums*nums

if __name__ == "__main__":
    
    numbers = range(10)
    pool = Pool()
    
    # imp pool methods
    # map, apply, join, close
    
    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0])              
    
    pool.close()
    pool.join()
    
    print(result)