import threading
import time

flag_exit = False  #true 일경우, 9줄에서 쓰레드가 종료되도록 합니다.

def t1_main():
    while True:
        print("\tt1")
        time.sleep(0.5)
        if flag_exit: break
t1 = threading.Tread(target=t1_main)
t1.start()

try:
    while True:
        print("main")
        time.sleep(1.0)

except KeyboardInterrupt:
    pass

flag_exit = True
t1.join()