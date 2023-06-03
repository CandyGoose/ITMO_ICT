'''
сценарий, когда требуется распределить задачи получения
веб-страниц на несколько потоков
'''

import time
import threading
import urllib.request
from queue import Queue

class Consumer(threading.Thread):
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self._queue = queue

	def run(self):
		while True:
			content = self._queue.get()
			if isinstance(content, str) and content == 'quit':
				break
			response = urllib.request.urlopen(content)
		print('Bye byes!')


def Producer():
	urls = [
		'http://www.python.org', 'http://www.yahoo.com',
		'http://www.scala.org', 'http://www.google.com'
		]
	queue = Queue()
	worker_threads = build_worker_pool(queue, 4)
	start_time = time.time()

	# Add the urls to process
	for url in urls:
		queue.put(url)	
	# Add the poison pillv
	for worker in worker_threads:
		queue.put('quit')
	for worker in worker_threads:
		worker.join()

	print('Done! Time taken: {}'.format(time.time() - start_time))

def build_worker_pool(queue, size):
	workers = []
	for _ in range(size):
		worker = Consumer(queue)
		worker.start()
		workers.append(worker)
	return workers

if __name__ == '__main__':
	Producer()
