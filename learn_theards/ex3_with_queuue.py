import os
import threading
import urllib.request
from queue import Queue
 
 
class Downloader(threading.Thread):    
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        while True:
            # Get url from queue
            url = self.queue.get()
            
            # Load file
            self.download_file(url)
            
            # Recieve signal thet task is ready
            self.queue.task_done()
 
    def download_file(self, url):
        handle = urllib.request.urlopen(url)
        fname = os.path.basename(url)
        
        with open(fname, "wb") as f:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f.write(chunk)
 
def main(urls):
    queue = Queue()
    
    # Запускаем потом и очередь
    for i in range(5):
        t = Downloader(queue)
        t.setDaemon(True)
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
