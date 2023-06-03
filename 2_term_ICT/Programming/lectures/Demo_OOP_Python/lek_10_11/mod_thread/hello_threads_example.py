import threading
import datetime
        
class ThreadClass(threading.Thread):
   def run(self):
       now = datetime.datetime.now()
       print("%s says Hello World at time: %s\n" % (self.getName(), now))

print(threading.activeCount())     # 2
print(threading.enumerate())       # [<_MainThread(MainThread, started 5944)>, <Thread(SockThread, started daemon 7120)>]
"""
IDLE обменивается данными через сокет, а интерактивныый интерпретатор, им предоставлямый
использует поток-демон для выполнения фоновой связи с сокетом
"""

for i in range(10):
  t = ThreadClass()
  t.start()

print(threading.enumerate())
