import multiprocessing
import datetime

def Process1(args):
    print("Square : {}".format(args*args))
    print("Process_time_1 :  {}".format(datetime.datetime.now()))

def Process2(args):
    print("Cube : {}".format(args*args*args))
    print("Process_time_2: {}".format(datetime.datetime.now()))

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=Process1, args=(10,))
    p2 = multiprocessing.Process(target=Process2, args=(10,))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    print("Finished..")