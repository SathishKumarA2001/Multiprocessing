import multiprocessing

def num(list,q):
    for i in list:
        q.put(i)

def print_q(q):
    while not q.empty():
        print(q.get())

if __name__ == '__main__':
    list = [1,2,3,4]
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=num,args=(list,q))
    p2 = multiprocessing.Process(target=print_q,args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print("Completed!")