import time,os
from multiprocessing import Process,current_process
from threading import Thread,current_thread

count = 200000000
SLEEP = 10

def io_bound(sec):
    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name
    print(f"{pid} * {thread_name} * {process_name} \ ---->Start Sleeping...")
    time.sleep(sec)
    print(f"{pid} * {thread_name} * {process_name} \ ---->Fininshed Sleeping...")

def cpu_bound(n):
    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name
    print(f"{pid} * {thread_name} * {process_name} \ ---->Start Sleeping...")
    
    while n>0:
        n-=1
    
    print(f"{pid} * {thread_name} * {process_name} \ ---->Fininshed Sleeping...")

if __name__ =='__main__':
    start = time.time()
    
    # 1st snippet --> Running IO-bound task twice, one after the other…
    #io_bound(SLEEP)
    #io_bound(SLEEP)
    ##########
   # 2nd snippet --> Using threading to run the IO-bound tasks…
    #t1 = Thread(target=io_bound,args=(SLEEP,))
    #t2 = Thread(target=io_bound,args=(SLEEP,))
    #t1.start()
    #t2.start()
    #t1.join()
    #t2.join() 
    ##########
    # 3rd snippet --> Running CPU-bound task twice with operations, one after the other…
    #cpu_bound(count)
    #cpu_bound(count)
    ##########
    # 4th snippet --> Can threading to run the CPU-bound tasks with operation fastly? No it doesn't ...
    #t1 = Thread(target=cpu_bound, args =(count, ))
    #t2 = Thread(target=cpu_bound, args =(count, ))
    #t1.start()
    #t2.start()
    #t1.join()
    #t2.join()
    ##########
    # 5th snippet --> so, does spilliting the tasks as two process can speed up than threading? yes it does...
    #p1 = Process(target = cpu_bound, args =(count, ))
    #p2 = Process(target = cpu_bound, args =(count, ))
    #p1.start()
    #p2.start()
    #p1.join()
    #p2.join()
    ##########
    # 6th snippet --> let's spilliting the tasks as two process in io_bounds...
    p1 = Process(target = io_bound, args =(SLEEP, ))
    p2 = Process(target = io_bound, args =(SLEEP, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


    end = time.time()
    print("Time taken in seconds : -",end-start)
    