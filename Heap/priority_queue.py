# Similar to the heap code. The only different is in accessing the priority using an extra [0]
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, item, priority):
        self.heap.append((priority, item))
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty priority queue")
        
        # Swap first and last, remove the last (smallest priority)
        self._swap(0, len(self.heap) - 1)
        priority, item = self.heap.pop()
        self._heapify_down(0)
        return item

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[index][0] < self.heap[parent][0]:
            self._swap(index, parent)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.insert("clean house", 3)
    pq.insert("pay bills", 1)
    pq.insert("do homework", 2)

    while not pq.is_empty():
        print(pq.pop())
