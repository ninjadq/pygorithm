from collections import deque

class Stack(object):
    def __init__(self):
        self._dq = deque()

    def push(self, item):
        self._dq.append(item)

    def pop(self):
        return self._dq.pop()

    def is_empty(self):
        return len(self._dq) == 0

    def size(self):
        return len(self._dq)
        
