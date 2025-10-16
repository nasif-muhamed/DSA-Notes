# Note: This can also work as a priority queue due to the comparison behaviour of tuples in python
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            # Stop when parent is smaller (min-heap property)
            if self.heap[parent] <= self.heap[idx]:
                break
            # Swap and move up
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent

    def delete(self):
        if not self.heap:
            return None
        
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self._bubble_down(0)
        return min_val
    
    def _bubble_down(self, idx):
        smallest = idx
        left, right = (idx * 2) + 1, (idx * 2) + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if idx != smallest:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._bubble_down(smallest)

    def build_heap(self, arr):
        self.heap = arr[:]
        last_parent = (len(arr) // 2) - 1
        for i in range(last_parent, -1, -1):
            self._bubble_down(i)
