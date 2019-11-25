import multiprocessing as mp
import threading
import random
import time

rwMutex = threading.Semaphore(value=1)
mutex = threading.Semaphore(value=1)
readCount = 0
list = [0]

def writer():
    writerNumber = random.randrange(100)
    while True:
        time.sleep(random.randrange(3, 6))
        print(f"writer {writerNumber}: wait on rwMutex")
        rwMutex.acquire()
        print(f"writer {writerNumber}: in CS")
        list.append(list[-1] + 1)
        rwMutex.release()
        print(f"writer {writerNumber}: release rwMutex")

def reader():
    global readCount
    readerNumber = random.randrange(100)
    while True:
        time.sleep(random.randrange(3, 6))
        print(f"reader {readerNumber}: wait on mutex")
        mutex.acquire()
        print(f"reader {readerNumber}: in CS for mutex")
        readCount += 1
        if readCount == 1:
            print(f"reader {readerNumber}: wait on rwMutex")
            rwMutex.acquire()
            print(f"reader {readerNumber}: in CS for rwMutex")

        mutex.release()
        print(f"reader {readerNumber}: release mutex")
        print(list)
        print(f"reader {readerNumber}: wait on mutex")
        mutex.acquire()
        print(f"reader {readerNumber}: in CS for mutex")
        readCount -= 1
        if readCount == 0:
            rwMutex.release()
            print(f"reader {readerNumber}: release rwMutex")
        mutex.release()
        print(f"reader {readerNumber}: release mutex")


if __name__ == '__main__':
    pool = mp.Pool(mp.cpu_count())
    writerCount = int(input("How many writer?"))
    readerCount = int(input("How many reader?"))
    for i in range(writerCount):
        pool.apply_async(writer)
    for i in range(readerCount):
        pool.apply_async(reader)
    pool.close()
    pool.join()
