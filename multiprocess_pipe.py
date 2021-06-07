import multiprocessing
from multiprocessing import process
import os

def sender(conn,msgs):
    for msg in msgs:
        conn.send(msg)
        print("Msg to be send: ",msg)
    conn.close()

def receiver(conn):
    try:    
        while 1:
            msg = conn.recv()
            print("Recieved from sender: ",msg)
            if msg == 'END':
                conn.close()
        
    except OSError as er:
            print("Exception connection end: ",er)

if __name__=='__main__':
    msgs = ['Hey','Hoy','Hello','Hola','END']
    
    sender_conn,receiver_conn = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=sender,args=(sender_conn,msgs))
    p2 = multiprocessing.Process(target=receiver,args=(receiver_conn,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()