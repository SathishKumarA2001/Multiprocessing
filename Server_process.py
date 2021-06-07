import multiprocessing

def print_records(records):
    for i in records:
        print("Name : {} and id : {}".format(i[0],i[1]))

def insert_record(record,records):
    records.append(record)

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        records = manager.list([('sam',2),('rock',3),('dot',5)])
        record = ('chal',4)
        
        p1 = multiprocessing.Process(target=insert_record,args=(record,records))
        p2 = multiprocessing.Process(target=print_records,args=(records,))

        p1.start()
        p1.join()

        p2.start()
        p2.join()