'''
реализация потоков демонов
Как вы можете видеть, приложение продолжает работать, даже после того,
как главный поток завершился (сообщение: “App stop”)
'''

import threading
import time

def func():
   for i in range(5):
      print(f"from child thread: {i}")
      time.sleep(0.5)

th = threading.Thread(target=func) # daemon=True
th.start()

print("App stop")
