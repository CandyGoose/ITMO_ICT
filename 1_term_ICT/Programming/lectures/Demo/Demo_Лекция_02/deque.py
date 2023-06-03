"""Как использовать collections.deque 
"""
from collections import deque

q = deque()
 
q.append('eat')
q.append('sleep')
q.append('code')
q.appendleft('name')
 
print(q)        # deque(['name', 'eat', 'sleep', 'code'])

print(q.popleft()) # 'name'
print(q.popleft()) # 'eat'
print(q.pop()) # 'sleep'

 



