from collections import deque

class Queue(object):
    def __init__(self):
        self._q = deque()

    def enqueue(self, item):
        self._q.append(item)

    def dequeue(self):
        return self._q.popleft()

    def is_empty(self):
        return len(self._q) == 0

    def size(self):
        return len(self._q)
