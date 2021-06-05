import multiprocessing
import os

def Process1():
    print("Id Of running process 1 : {}".format(os.getpid()))

def Process2():
    print("Id of running Process 2 : {}".format(os.getpid()))

if __name__ == "__main__":
    print("Id of main Process : {}".format(os.getpid()))
    #Assigning the process 
    p1 = multiprocessing.Process(target=Process1)
    p2 = multiprocessing.Process(target=Process2)
    #start Process
    p1.start()
    p2.start()
    #Process Id
    print("Id of process 1 : {}".format(p1.pid))
    print("Id of Process 2 : {}".format(p2.pid))
    #waiting for the process finish
    p1.join()
    p2.join()
    print("Process fininshed...")
    #check if the process is alive
    print("Process alive 1: {}".format(p1.is_alive()))
    print("Process alive 2: {}".format(p2.is_alive()))
