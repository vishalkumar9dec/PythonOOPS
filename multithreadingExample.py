from time import sleep
from threading import *

class T(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)

class X(Thread):
    def run(self):
        for i in range(5):
            print('HI')
            sleep(1)

t1 = T()
x1 = X()

t1.start()
sleep(0.2)
x1.start()

t1.join()
x1.join()

print('Bye')