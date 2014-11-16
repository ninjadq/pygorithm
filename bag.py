class BagNode:
    def __init__(self,value = None):
        self._value = value
        self._next = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next_node(self):
        return self._next

    @next_node.setter
    def next_node(self, value):
        self._next = value


class Bag:
    def __init__(self):
        self._bag = BagNode()
        self.node = self._bag
        self._count = 0

    def add(self, item):
        new_node = BagNode(item)
        self.node.next_node = new_node
        self.node = self.node.next_node
        self._count += 1
            

    def size(self):
        return self._count

    def __iter__(self):
        self.current = self._bag.next_node
        return self

    def next(self):
        if self.current is not None:
            v = self.current.value
            self.current = self.current.next_node
            return v
        else:
            raise StopIteration
