import os
import threading
import urllib.request
from queue import Queue
 
 
class Downloader(threading.Thread):
    """Потоковый загрузчик файлов"""
    
    def __init__(self, queue):
        """Инициализация потока"""
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        """Запуск потока"""
        while True:
            # Получаем url из очереди
            url = self.queue.get()
            
            # Скачиваем файл
            self.download_file(url)
            
            # Отправляем сигнал о том, что задача завершена
            self.queue.task_done()
 
    def download_file(self, url):
        """Скачиваем файл"""
        handle = urllib.request.urlopen(url)
        fname = os.path.basename(url)
        
        with open(fname, "wb") as f:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f.write(chunk)
 
def main(urls):
    """
    Запускаем программу
    """
    queue = Queue()
    
    # Запускаем потом и очередь
    for i in range(5):
        t = Downloader(queue)
        t.setDaemon(True) # демонизированные потоки
        t.start()
    
    # Даем очереди нужные нам ссылки для скачивания
    for url in urls:
        queue.put(url)
 
    # Ждем завершения работы очереди
    queue.join()
 
if __name__ == "__main__":
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    
    main(urls)
