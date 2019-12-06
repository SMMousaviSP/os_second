import multiprocessing as mp
import threading
import random
import time

def producer():
    global empty
    # global mutex
    # global buffer
    # global full
    # while True:
    time.sleep(random.randrange(3, 6))
    item = random.randrange(1, 1000)
    empty.acquire()
    mutex.acquire()
    buffer.append(item)
    mutex.release()
    full.release()

def consumer():
    global empty
    # global mutex
    # global buffer
    # global full
    # while True:
    time.sleep(random.randrange(3, 6))
    full.acquire()
    mutex.acquire()
    item = buffer.pop()
    mutex.release()
    empty.release()
    print(f"consume {item}")


if __name__ == '__main__':
    pool = mp.Pool(mp.cpu_count())
    n = int(input("Size of limited buffer?"))
    mutex = threading.Semaphore(value=1)
    empty = threading.Semaphore(value=n)
    full = threading.Semaphore(value=0)
    producerCount = int(input("How many producer?"))
    consumerCount = int(input("How many consumer?"))
    buffer = []
    for i in range(producerCount):
        pool.apply(producer)
    for i in range(consumerCount):
        pool.apply(consumer)
    pool.close()
    pool.join()
    # producer()
    # consumer()
