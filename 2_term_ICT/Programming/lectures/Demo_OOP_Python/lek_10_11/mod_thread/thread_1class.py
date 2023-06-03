# Метод «классовый»
# Пример многопоточности Python для печати текущей даты.
# 1. Определите подкласс, используя класс Thread.
# 2. Создайте объект и запустите поток.

import threading
import datetime

class myThread (threading.Thread):
   def __init__(self, name, counter, daemon):
       threading.Thread.__init__(self)
       self.threadID = counter
       self.name = name
       self.counter = counter
       self.daemon = daemon # Назначить поток демоном

   def run(self):
       print("Starting " + self.name + ", id =  " + str(self.ident) + "\n")
       print_date(self.name, self.counter)
       print("Exiting " + self.name + "\n")
       """
       У каждого потока, пока он работает, есть
       уникальный идентификационный номер, который хранится в переменной ident
       """

def print_date(threadName, counter):
   datefields = []
   today = datetime.date.today()
   datefields.append(today)
   print("\n%s[%d]: %s" % ( threadName, counter, datefields[0]))

# Создать 
thread1 = myThread("Thread", 1, True)# Назначить поток демоном
thread2 = myThread("Thread", 2, False)

# Запустить 
thread1.start()
thread2.start()

print(thread1.isDaemon())
print(thread2.isDaemon())

thread1.join()
thread2.join()
print("Exiting the Program!!!")

