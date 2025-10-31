class Node:
    def __init__(self, val):
        self.val = val
        self.ref = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueu(self, val):
        new_node = Node(val)
        if not self.front:
            self.front = new_node
        if self.rear:
            self.rear.ref = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise Exception('Empty list')
        pop_val = self.front.val
        self.front = self.front.ref
        if self.front is None:
            self.rear = None
        return pop_val