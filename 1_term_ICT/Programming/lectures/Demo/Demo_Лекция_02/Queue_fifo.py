"""FIFO Queue
"""
import queue

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())


# Как использовать список Python в качестве очереди FIFO:
 
q = []
 
q.append('eat')
q.append('sleep')
q.append('code')
 
print(q)
# ['eat', 'sleep', 'code']
 
# Осторожнее: медленно работает!
print(q.pop(0)) # 'eat'
