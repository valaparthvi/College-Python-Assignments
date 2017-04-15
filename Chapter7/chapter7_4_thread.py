import time
from threading import Thread


def myfunc(i):
    print ("sleeping 5 sec from thread %d" % i)
    time.sleep(5)
    print("finished sleeping from thread %d" % i)


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=myfunc, args=(i,))
        t.start()

'''
Output: python3 chapter7_4_thread.py 
sleeping 5 sec from thread 0
sleeping 5 sec from thread 1
sleeping 5 sec from thread 2
sleeping 5 sec from thread 3
sleeping 5 sec from thread 4
sleeping 5 sec from thread 5
sleeping 5 sec from thread 6
sleeping 5 sec from thread 7
sleeping 5 sec from thread 8
sleeping 5 sec from thread 9
finished sleeping from thread 0
finished sleeping from thread 6
finished sleeping from thread 1
finished sleeping from thread 2
finished sleeping from thread 5
finished sleeping from thread 8
finished sleeping from thread 3
finished sleeping from thread 4
finished sleeping from thread 9
finished sleeping from thread 7
'''