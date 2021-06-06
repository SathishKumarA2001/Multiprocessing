import multiprocessing

output = []

def cube(list):
    for l in list:
        output.append(l*l*l)
    print("The result of Process 1 : {}".format(output))

if __name__ == '__main__':
    list = [1,2,3,4]
    process1 = multiprocessing.Process(target=cube,args=(list,))
    process1.start()
    process1.join()
    print("The result of main : {}".format(output))