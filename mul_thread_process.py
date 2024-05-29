import os
import time
from multiprocessing import Process

def square_numbers():
    print(f"PID of process: {os.getpid()}")
    for i in range(3):
        i * i
        time.sleep(0.1)

if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    # Create Processes
    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    # Start
    for p in processes:
        print("start")
        p.start()

    # Join
    for p in processes:
        print("join")
        p.join()

    print('Completed')
