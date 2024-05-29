from threading import Thread, Lock
import time

database_value = 0
def increase(lock):
    lock.acquire()
    global database_value
    local_copy = database_value+1
    time.sleep(0.1)
    database_value=local_copy
    lock.release()
    

if __name__ == "__main__":
    lock = Lock()
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print("Database value is " +str(database_value))