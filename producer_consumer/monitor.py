import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time

class Monitor:
    def __init__(self):
        self.lock = threading.Lock()
        self.buffer = []

    def produce(self):
        self.lock.acquire()
        item = random.randrange(100, 1000)
        print(f"producer: produce {item}")
        self.buffer.append(item)
        self.lock.release()

    def consume(self):
        self.lock.acquire()
        print(f"consumer: consume {self.buffer.pop()}")
        self.lock.release()

def producer():
    global m
    while True:
        time.sleep(1)
        item = random.randrange(1, 1000)
        print("producer: try to acquire empty")
        empty.acquire()
        print("producer: empty acquired")
        m.produce()
        full.release()
        print("producer: full released")

def consumer():
    global m
    while True:
        time.sleep(1)
        print("consumer: try to acquire full")
        full.acquire()
        print("consumer: full acquired")
        m.consume()
        empty.release()
        print("consumer: empty released")

m = Monitor()
n = int(input("Size of limited buffer?"))
mutex = threading.Semaphore(value=1)
empty = threading.Semaphore(value=n)
full = threading.Semaphore(value=0)
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(producer), executor.submit(consumer)}
        concurrent.futures.wait(futures)
