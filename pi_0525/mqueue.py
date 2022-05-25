import queue
import threading
import time

HOW_MANY_MESSAGES = 10
mq = queue.Queue(HOW_MANY_MESSAGES) #메시지 큐 만들기

flag_exit = False

def t1():
    value = 0

    while True:
        value = value+1
        mq.put(value)
        time.sleep(0.1)

        if flag_exit: break

tMQ = threading.Thread(target = t1)
tMQ.start()

try:
    while True:
        value = mq.get()
        print("Read Data %d"%value)

except KeyboardInterrupt:
    pass

flag_exit = True
tMQ.join()