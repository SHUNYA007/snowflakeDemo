import os
import time
import threading
import concurrent.futures




class UniqueIdGenerator:
    def __init__(self) -> None:
        self.output = {}
        self._atomic_counter = 0
        self._lock = threading.Lock()
        
    def increment(self):
        with self._lock:
            self._atomic_counter += 1

    def generateid(self):
        self.output.update({"time": int(time.time())})
        self.output.update({"processId": os.getpid()})
        self.increment()    
        self.output.update({"atomic counter": self._atomic_counter})    
        return self.output
    