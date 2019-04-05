class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1
        if self.current == self.capacity:
            self.current -= self.capacity

    def get(self):
        printer = []
        for item in self.storage:
            if item:
                printer.append(item)
        return printer
