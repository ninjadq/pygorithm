class MaxPQ(object):
    def __init__(self, lst = None):
        self.pq = [None]
        self.N = 0
        if lst is not None:
            for i in lst: self.insert(i)

    def insert(self, v):
        self.pq.append(v)
        self.N += 1
        self.__swim(self.N)

    def delMax(self):
        if self.isEmpty(): raise ValueError
        max_value = self.pq[1]
        self.pq[1], self.pq[self.N] = self.pq[self.N], self.pq[1]
        del(self.pq[self.N])
        self.N -= 1
        self.__sink(1)
        return max_value

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def __swim(self, index):
        while index > 1 and self.pq[index//2] < self.pq[index]:
            self.pq[index//2], self.pq[index] = self.pq[index], self.pq[index//2]
            index = index//2

    def __sink(self, index):
        while 2*index <= self.N:
            j = 2*index
            if j < self.N and self.pq[j] < self.pq[j+1]: j += 1
            if self.pq[index] >= self.pq[j]: break;
            self.pq[index], self.pq[j] = self.pq[j], self.pq[index]
            index = j


class MinPQ(object):

    def __init__(self, lst = None):
        self.pq = [None]
        self.N = 0
        if lst is not None:
            for i in lst: self.insert(i)

    def insert(self, v):
        self.pq.append(v)
        self.N += 1
        self.__swim(self.N)

    def delMin(self):
        if self.isEmpty(): raise ValueError
        min_value = self.pq[1]
        self.pq[1], self.pq[self.N] = self.pq[self.N], self.pq[1]
        del(self.pq[self.N])
        self.N -= 1
        self.__sink(1)
        return min_value

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def __swim(self, index):
        while index > 1 and self.pq[index//2] > self.pq[index]:
            self.pq[index//2], self.pq[index] = self.pq[index], self.pq[index//2]
            index = index//2

    def __sink(self, index):
        while 2*index <= self.N:
            j = 2*index
            if j < self.N and self.pq[j] > self.pq[j+1]: j += 1
            if self.pq[index] <= self.pq[j]: break;
            self.pq[index], self.pq[j] = self.pq[j], self.pq[index]
            index = j
