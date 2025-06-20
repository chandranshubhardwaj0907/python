import threading

import time

def worker():
    """Thread worker function."""
    print("Worker thread starting")
    time.sleep(2)
    print("Worker thread finished")
    
    
threads =[]
for i in range(3):
    thread = threading.Thread(target=worker,args=(i,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()  # Wait for the thread to finish
print("All threads have finished execution")        