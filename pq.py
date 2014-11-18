class MaxPQ(object):
    def __init__(self, lst = None):
        self.pq = []
        if lst is not None:
            for i in lst: self.insert()

    def insert(self, v):
        self.pq.append(v)
        self.__swim(len(self.pq)-1)

    def delMax(self):
        m = self.pq[0]
        self.pq[0], self.pq[len(self.pq)-1] = self.pq[len(self.pq)-1], self.pq[0]
        del(self.pq[len(self.pq)-1])
        self.__sink(0)
        return m

    def isEmpty(self):
        return len(self.pq) == 0

    def size(self):
        return len(self.pq)

    def __swim(self, index):
        while index != 0 and self.pq[index//2] < self.pq[index]:
            self.pq[index//2], self.pq[index] = self.pq[index], self.pq[index//2]
            index = index//2

    def __sink(self, index):
        while 2*index < len(self.pq):
            j = 2*index
            if j < len(self.pq)-1 and self.pq[j] < self.pq[j+1]: j += 1
            if self.pq[index] >= self.pq[j]: break;
            self.pq[index], self.pq[j] = self.pq[j], self.pq[index]
            index = j

