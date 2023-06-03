import os
import urllib.request
import requests
from threading import Thread
 
class DownloadThread(Thread):
    """
    Пример скачивание файла используя многопоточность
    """
    
    def __init__(self, url, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
        self.url = url
    
    def run(self):
        """Запуск потока"""
        handle = urllib.request.urlopen(self.url)
        fname = os.path.basename(self.url)
    
        with open(fname, "wb") as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f_handler.write(chunk)
        
        msg = "%s закончил загрузку %s!" % (self.name, self.url)
        print(msg)
 
 
def main(urls):
    """
    Запускаем программу
    """
    req = requests.get("http://www.irs.gov/pub")
    print(req)
    for item, url in enumerate(urls):
        name = "Поток %s" % (item+1)
        thread = DownloadThread(url, name)
        thread.start()
 
if __name__ == "__main__":
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
 
    main(urls)
