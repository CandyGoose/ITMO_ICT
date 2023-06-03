'''
реализация потоков демонов 
'''

import threading
import time

def nondaemonThread():
   print("starting my thread")
   time.sleep(8)
   print("ending my thread")

def daemonThread():
   while True:
       print("Hello")
       time.sleep(2)



if __name__ == '__main__':
   nondaemonThread = threading.Thread(target = nondaemonThread)

   daemonThread = threading.Thread(target = daemonThread)
   daemonThread.setDaemon(True)

   daemonThread.start()
   nondaemonThread.start()
