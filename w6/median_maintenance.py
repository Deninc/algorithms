
'''
Median Maintenance using heap
'''

class Heap():
    """integer heap data structure
    can be either min heap or max heap"""

    def __init__(self, min_heap=True):
        """default min = True for min heap"""
        self.heap = []
        self.min = min_heap

    @property
    def first(self):
        """get min/max node value without popping it out"""
        return self.heap[0]

    @property
    def length(self):
        """len of heap"""
        return len(self.heap)

    def push(self, k):
        """push node k to heap
        add k to the last index, bubble up if necessary"""
        self.heap.append(k)
        if self.min:
            self._bubbleup()
        else:
            self._bubbleup_max()

    def pop(self):
        """pop min/max node
        swap the last key to the top then bubble down"""
        last = self.heap.pop()  # raise error if empty
        if self.heap:
            res = self.heap[0]
            self.heap[0] = last
            if self.min:
                self._bubbledown()
            else:
                self._bubbledown_max()
        else:
            res = last
        return res

    def _bubbleup(self):
        """newly added last node go up the tree hierachy as necessary"""
        pos = len(self.heap) - 1    # index of new element
        par = self._parent(pos)
        while self.heap[par] > self.heap[pos]:
            self.heap[par], self.heap[pos] = self.heap[pos], self.heap[par]
            pos = par
            if pos == 0:
                break
            par = self._parent(pos)

    def _bubbledown(self):
        """the top node go down the tree hierachy as necessary"""
        pos = 0
        child = self._child(pos)
        while self.heap[pos] > self.heap[child]:
            self.heap[pos], self.heap[child] = self.heap[child], self.heap[pos]
            pos = child
            child = self._child(pos)
            if child == -1:
                break

    def _bubbleup_max(self):
        """same as bubbleup but for max heap"""
        pos = len(self.heap) - 1    # index of new element
        par = self._parent(pos)
        while self.heap[par] < self.heap[pos]:
            self.heap[par], self.heap[pos] = self.heap[pos], self.heap[par]
            pos = par
            if pos == 0:
                break
            par = self._parent(pos)

    def _bubbledown_max(self):
        """same as bubbledown but for max heap"""
        pos = 0
        child = self._child(pos, take_smaller=False)
        while self.heap[pos] < self.heap[child]:
            self.heap[pos], self.heap[child] = self.heap[child], self.heap[pos]
            pos = child
            child = self._child(pos, take_smaller=False)
            if child == -1:
                break

    def _parent(self, i):
        """index of parent of node indexed i"""
        return (i - 1) / 2 if i % 2 else (i - 2) / 2

    def _child(self, i, take_smaller=True):
        """index of smaller/larger child of node indexed i"""
        left, right = 2 * i + 1, 2 * i + 2
        last = len(self.heap) - 1
        if left <= last:
            if right <= last:
                if self.heap[left] <= self.heap[right]:
                    return left if take_smaller else right
                return right if take_smaller else left
            return left
        return -1

""" ALGORITHM
We keep two heaps:
    - max_heap: n/2 lowest numbers
    - min_heap: n/2 highest numbers
    -> max_heap[0] < min_heap[0]
for each new number x, add it to max_heap if x < max_heap[0]
                    or add it to min_heap if x > min_heap[0]
max_heap[0]: highest number of lowest half -> median of n numbers
min_heap[0]: lowest number of top half -> median of n numbers
"""

def get_medians(stream):
    min_heap = Heap()
    max_heap = Heap(min_heap=False)
    max_heap.push(stream[0])
    n = len(stream)
    medians = [stream[0]]

    for i in range(1, n):
        x = stream[i]
        if x < max_heap.first:
            max_heap.push(x)
        else:
            min_heap.push(x)
        # rebalance two heaps to the same n/2 items
        if min_heap.length - max_heap.length > 1:
            item = min_heap.pop()
            max_heap.push(item)
        elif max_heap.length - min_heap.length > 1:
            item = max_heap.pop()
            min_heap.push(item)
        # i+1 is total numbers added
        if (i+1) % 2 == 0 or max_heap.length > min_heap.length:
            medians.append(max_heap.first)
        else:
            medians.append(min_heap.first)

    return medians

# if __name__ == "__main__":
#     with open("w6/median.txt") as f:
#         stream = f.readlines()
#     stream = map(int, stream)
#     medians = get_medians(stream)
#     assert len(stream) == len(medians)
#     print sum(medians)
