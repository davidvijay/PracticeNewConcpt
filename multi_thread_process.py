import os
import time
import psutil
from multiprocessing import Process

def square_numbers():
    print(f"PID of process: {os.getpid()}")
    for i in range(100):
        i*i
        time.sleep(0.1)
        
processes = []
num_processes = os.cpu_count()

# Create Processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)
    
# Start
for p in processes:
    p.start()
    
# Join
for p in processes:
    p.join()
    
print('Completed')
