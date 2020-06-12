from collections import deque


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.remaining = capacity

    def append(self, item):
        self.remaining -= 1
        q = deque()

        if self.remaining <= self.capacity and self.remaining >= 0:
            q.append(item)
        elif self.remaining < 0:
            q.popleft()
            q.append(item)
        return q

    def get(self):
        pass
