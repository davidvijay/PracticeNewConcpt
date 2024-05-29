from threading import Thread, Lock
import time

# def cubenumbers(i):
#     print(i*i)
#     time.sleep(1)
    
    

# #creation
# num_threads = 10
# threads=[]
# for i in range(num_threads):
#     t=Thread(target=cubenumbers, args=(10,))
#     threads.append(t)
#     t.start()


# #Join
# for t in threads:
#     t.join()
    
    
Database_value = 0

def changing_values(lock):
    global Database_value
    with lock:
        copy_value=Database_value+1
        time.sleep(0.1)
        Database_value=copy_value
        
    
    
#creation
num_threads=2
threads=[]
lock=Lock()
for i in range(num_threads):
    t=Thread(target=changing_values, args=(lock,))
    threads.append(t)
    t.start()
    
for j in threads:
    j.join()

print(Database_value)