import threading
import time


def hello():
    for i in range(5):
        print('hello')
        time.sleep(1)

def world():
    for i in range(5):
        print('world')
        time.sleep(2)

thread1 = threading.Thread(target=hello)
thread2 = threading.Thread(target=world)

print(thread1.is_alive())
print(thread2.is_alive())

thread1.start()
thread2.start()
