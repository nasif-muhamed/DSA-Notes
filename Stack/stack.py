class Node:
    def __init__(self, val):
        self.val = val
        self.ref = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = Node(val)
        new_node.ref = self.top 
        self.top = new_node

    def pop(self):
        if not self.top:
            raise Exception('Empty List')
        pop_value = self.pop.val
        self.top = self.top.ref
        return pop_value
