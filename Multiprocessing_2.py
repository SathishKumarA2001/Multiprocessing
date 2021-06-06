import multiprocessing

def cube(list,result,value):
    for rdx,num in enumerate(list):
        result[rdx] = num * num * num
        
    value.value = sum(result)

    print("Process 1 result : {}".format(result[:]))
    print("Process 1 sum_cube : {}".format(value.value))

if __name__ == '__main__':
    list = [1,2,3,4]
    result = multiprocessing.Array('i',4)
    value = multiprocessing.Value('i')

    process1 = multiprocessing.Process(target=cube,args=(list,result,value))
    process1.start()
    process1.join()
    print("The result of main : {}".format(result[:]))
    print("The value of main : {}".format(value.value))
    