# from threading import Thread
# import os

# def square(i):
#     print(f"i value is {i} and its square is: {i*i}")
    
# #create process
# num_thread = os.cpu_count()
# for i in range(num_thread):
#     t = Thread(target=square, args=(i,))
#     t.start()

# for i in range(num_thread):
#     t.join()

# print('end_main')

from threading import Thread, current_thread, Lock
from queue import Queue




def square_num(lock):
    while True:
        value = q.get()
        with lock:
            print(f"current thread name is{current_thread().name} got {value}")
        q.task_done()

#Thread creation
if __name__ == "__main__":
    q=Queue()
    threads =[]
    num_threads =4
    lock =Lock()
    for i in range(num_threads):
        t= Thread(target=square_num, args=(lock,))
        threads.append(t)
        t.daemon=True
        t.start()
    
    for k in range(21):
        q.put(k)
    #Wait until the entire thread needs to be completed 
    q.join()
        


    
