# import multiprocessing as mp
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time

def producer():
    global buffer
    while True:
        time.sleep(1)
        item = random.randrange(1, 1000)
        print("producer: try to acquire empty")
        empty.acquire()
        print("producer: empty acquired, try to acquire mutex")
        mutex.acquire()
        print("producer: mutex acquired")
        print(f"producer: produce: {item}")
        buffer.append(item)
        mutex.release()
        print("producer: mutex released")
        full.release()
        print("producer: full released")

def consumer():
    print("consumer: IN")
    global buffer
    while True:
        time.sleep(1)
        print("consumer: try to acquire full")
        full.acquire()
        print("consumer: full acquired, try to acquire mutex")
        mutex.acquire()
        item = buffer.pop()
        mutex.release()
        print("consumer: mutex released")
        empty.release()
        print("consumer: empty released")
        print(f"consumer: consume: {item}")




n = int(input("Size of limited buffer?"))
mutex = threading.Semaphore(value=1)
empty = threading.Semaphore(value=n)
full = threading.Semaphore(value=0)
buffer = []
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(producer), executor.submit(consumer)}
        concurrent.futures.wait(futures)
