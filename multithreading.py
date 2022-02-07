from concurrent.futures import thread
from threading import Thread
import os

def square_num():
    for i in range(100):
        i*i

if __name__ == "__main__":    
    threads = []
    num_threads = 10

    # create threads
    for i in range(num_threads):
        t = Thread(target = square_num)
        threads.append(t)
        
    # start
    for t in threads:
        t.start()
        
    # join
    for t in threads:
        t.join()
        
    print("end main")
    
    
    
    
# sharing variable between threads
from threading import Thread
import os
import time

database_value = 0     # defining global variable

def increase():
    global database_value      # way to use global variable woth "global" keyword

    local_copy = database_value
    # processing
    local_copy += 1
    time.sleep(0.1)                # thread1 will sleep for 0.1 and thread2 starts
    database_value = local_copy    # due to this race condtion will occur 
                                   # as both thread works on same variable
if __name__ == "__main__":
    print("start value: ", database_value)
    
    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print("end value: ", database_value)
    
    print("end main")
    
    
    
    
    
# to prevent above issue
from threading import Thread, Lock
import time

database_value = 0     # defining global variable

def increase(lock):            # locks the state and doesn't shift to thread2 since thread1 is completed
    global database_value      # way to use global variable woth "global" keyword

    lock.acquire()
    local_copy = database_value
    # processing
    local_copy += 1
    time.sleep(0.1)                
    database_value = local_copy    
    lock.release()
    
    # # alternative for above code
    # with lock:
    #     local_copy = database_value
    #     # processing
    #     local_copy += 1
    #     time.sleep(0.1)                
    #     database_value = local_copy 
    
if __name__ == "__main__":
    
    lock = Lock()
    print("start value: ", database_value)
    
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print("end value: ", database_value)
    
    print("end main")
    
    
    
    
# some threading functions in python
if __name__ == "__main__":
    
    q = Queue()
    
    q.put(1)
    q.put(2)
    q.put(3)
    
    first = q.get()
    print(first)
    
    q.task_done()   # should be done after working with a thread
    q.join()        # blocks until all items in queue have been processed
    
    q.empty()      # checks empty queue
    
    print("end main")
    
    
    
    
# queues are best for threading in python
from threading import Thread, Lock, current_thread
from queue import Queue
import time

def worker(q, lock):
    while True:
        value = q.get()
        
        with lock:
            print(f"in{current_thread().name} got {value}")
        q.task_done()
        
if __name__ == "__main__":
    
    q = Queue()
    lock = Lock()
    num_threads = 10
    
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True
        thread.start()
        
    for i in range(1, 21):
        q.put(i)
        
    q. join
    
    print("end main")