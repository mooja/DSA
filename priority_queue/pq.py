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
        pass

    def _exch(self, idx1, idx2):
        self.pq[idx1], self.pq[idx2] = self.pq[idx2], self.pq[idx1]

    def _sink(self, idx):
        pass

    def _swim(self, idx):
        while idx > 1:
            item = self.pq[idx]
            parent = self.pq[idx//2]
            if parent >= item:
                return
            self._exch(idx, idx//2)
            idx = idx // 2


if __name__ == "__main__":
    pq = PQ()
    pq.insert(1);
    pq.insert(2);
    pq.insert(0);
    pq.insert(5);
    from pprint import pprint
    pprint(pq.pq)
