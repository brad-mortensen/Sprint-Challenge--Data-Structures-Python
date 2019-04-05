class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):        
        if not self.storage[self.current]:
            self.storage.append(item)
            self.current += 1
            if self.current == self.capacity:
                self.current -= self.capacity

    def get(self):
        return self.storage
