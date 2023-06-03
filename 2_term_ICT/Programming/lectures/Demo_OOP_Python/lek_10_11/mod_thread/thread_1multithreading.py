# Демонстрация блокировки 
# 1. Определите подкласс, используя класс Thread. 
# 2. Создайте подкласс и запустите поток. 
# 3. Реализуйте блокировки в методе выполнения потока.

import threading
import datetime

Flag = 0

class myThread (threading.Thread):
   def __init__(self, name, counter):
       threading.Thread.__init__(self)
       self.threadID = counter
       self.name = name
       self.counter = counter

   def run(self):
       print("Starting " + self.name + "\n")

       # Получить блокировку для синхронизации потока
       threadLock.acquire()
       print_date(self.name, self.counter)

       # Снять блокировку для следующего потока
       threadLock.release()
       print("Exiting " + self.name + "\n")

def print_date(threadName, counter):
   datefields = []
   today = datetime.date.today()
   datefields.append(today)
   print("%s[%d]: %s" % (threadName, counter, datefields[0]))

threadLock = threading.Lock()
threads = []

# создать потоки
thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 2)

# Запустить потоки
thread1.start()
thread2.start()

# Добавить потоки в список
threads.append(thread1)
threads.append(thread2)

# Дождитесь завершения всех потоков
for t in threads:
   t.join()

print("Exiting the Program!!!")
