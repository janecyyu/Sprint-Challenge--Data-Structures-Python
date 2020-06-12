from collections import deque


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0
        self.data = deque()

    def append(self, item):
        if self.index < self.capacity:
            self.data.append(item)
        else:
            self.data[self.index % self.capacity] = item
        self.index += 1

    def get(self):
        result = []
        for i in self.data:
            result.append(i)
        return result

# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.data = []
#         self.index = 0

#     def append(self, item):
#         if self.index < self.capacity:
#             self.data.append(item)
#         else:
#             self.data[self.index % self.capacity] = item
#         self.index += 1

#     def get(self):
#         return self.data
