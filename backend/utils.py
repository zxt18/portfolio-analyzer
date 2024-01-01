import time 

class TimedCache:
    def __init__(self, expiry_seconds):
        self.expiry_seconds = expiry_seconds
        self.cache = {}
        
    def __setitem__(self, key, value): 
        self.cache[key] = {'value': value, 'expiry': time.time() + self.expiry_seconds}
        
    def __getitem__(self, key):
        if key in self.cache and time.time() < self.cache[key]['expiry'] : 
            return self.cache[key]
        return None
    
    def delete_cache(self) : 
        current_time = time.time()
        for key, val in self.cache.items() : 
            if current_time > val["expiry"]  :
                del self.cache[key]