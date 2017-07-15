#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class PQ(object):

    """An implementation of Max Priority Queue"""

    def __init__(self):
        self.pq = [None]
        self.size = 0

    def insert(self, item):
        self.pq.append(item)
        self.size += 1
        self._swim(self.size)

    def del_max(self):
        if not self.size > 0:
            raise IndexError
        rv = self.pq[1]
        self._exch(1, self.size)
        self.pq.pop()
        self.size -= 1
        self._sink(1)
        return rv

    def _exch(self, idx1, idx2):
        self.pq[idx1], self.pq[idx2] = self.pq[idx2], self.pq[idx1]

    def _sink(self, idx):
        while idx*2 < self.size:
            item = self.pq[idx]
            only_one_child = idx*2+1 > self.size
            if only_one_child:
                child = self.pq[idx*2]
                if child <= item:
                    return
                self._exch(idx, idx*2)
                idx = idx*2
            else:
                child1 = self.pq[idx*2]
                child2 = self.pq[idx*2+1]
                if not (child1 > item or child2 > item):
                    return
                bigger_child_idx = idx*2 if child1 > child2 else idx*2+1
                self._exch(idx, bigger_child_idx)
                idx = bigger_child_idx

    def _swim(self, idx):
        while idx > 1:
            item = self.pq[idx]
            parent = self.pq[idx//2]
            if parent >= item:
                return
            self._exch(idx, idx//2)
            idx = idx // 2


if __name__ == "__main__":
    import random
    from pprint import pprint
    pq = PQ()
    numbers = list(range(0, 15))
    random.shuffle(numbers)
    pprint(numbers)
    for n in numbers:
        pq.insert(n)
    pprint(pq.pq)
    while pq.size > 1:
        pprint(pq.del_max())
