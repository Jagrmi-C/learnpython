import os

from urllib.request import urlopen
from threading import Thread
 
class DownloadThread(Thread):
    
    def __init__(self, url, name):
        Thread.__init__(self)
        self.name = name
        self.url = url
    
    def run(self):
        handle = urlopen(self.url)
        fname = os.path.basename(self.url)
        
        with open(fname, "wb") as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f_handler.write(chunk)
        
        msg = "%s finished load %s!" % (self.name, self.url)
        print(msg)
 
 
def main(urls):
    """
    Run the program
    """
    for item, url in enumerate(urls):
        name = "Theard %s" % (item+1)
        thread = DownloadThread(url, name)
        thread.start()
 
if __name__ == "__main__":
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    
    main(urls)
