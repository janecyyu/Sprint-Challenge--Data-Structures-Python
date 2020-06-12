from collections import deque


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index = 0

    def append(self, item):
        if self.index < self.capacity:
            self.data.append(item)
        else:
            self.data[self.index % self.capacity] = item
        self.index += 1

    def get(self):
        return self.data


ring = RingBuffer(3)
ring.append(1)
ring.append(2)
print(ring)
