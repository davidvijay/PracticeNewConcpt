from threading import Thread

def square_numbers():
    print("Enter Function")
    for i in range(10):
        i*i

#Thread creation
if __name__=="__main__":
    threads =[]
    num_threads = 10
    
    for i in range(num_threads):
        t = Thread(target=square_numbers)
        threads.append(t)
    
    for j in threads:
        j.start()
        
    for j in threads:
        j.join()
        
        
    