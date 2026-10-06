class LRUCache:

    def __init__(self, capacity: int):
        self.ru = []
        self.lru_cache = collections.defaultdict(lambda: -1)
        self.iter_idx = 0
        self.capacity = capacity
        
    def update(self, key: int) -> None:
        if key in self.ru:
            self.ru.remove(key)
        self.ru.append(key)

    def evict(self):
        return self.ru.pop(0)

    def get(self, key: int) -> int:
        # print(f'before get: {self.ru}')        
        if self.lru_cache[key] != -1:
            self.update(key)
            # print(f'after get: {self.ru}')        
            return self.lru_cache[key]
        # print(f'after get: {self.ru}')        
        return -1
        

    def put(self, key: int, value: int) -> None:
        # print(f'before put: {self.ru}')
        if self.lru_cache[key] != -1:
            self.update(key)
            self.lru_cache[key] = value
        else:
            self.update(key)
            if len(self.ru) > self.capacity: 
                # print(f'ru before evict: {self.ru}')
                evict_target = self.evict()
                # print(f'evict_target: {evict_target}')
                # print(f'ru after evict: {self.ru}')
                self.lru_cache[evict_target] = -1        
            self.lru_cache[key] = value
        # print(f'after put: {self.ru}')        
        
