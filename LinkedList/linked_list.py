class Node:
    def __init__(self, val, ref=None):
        self.val = val
        self.ref = ref


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_begin(self, val):
        new_node = Node(val, self.head)
        self.head = new_node

    def add_end(self, val):
        new_node = Node(val)
        curr = self.head
        if curr is None:
            self.head = new_node
            return
        while curr.ref:
            curr = curr.ref
        curr.ref = new_node

    def add_after(self, val, after):
        curr = self.head
        while curr:
            if curr.val == after:
                temp = curr.ref
                curr.ref = Node(val, temp)
                return
            curr = curr.ref
        raise Exception('Target not found')
    
    def add_before(self, val, before):
        curr = self.head
        prev = None
        while curr:
            if curr.val == before:
                new_node = Node(val, curr)
                if prev is None:
                    self.head = new_node
                else:
                    prev.ref = new_node
                return
            prev = curr
            curr = curr.ref
        raise Exception('Target not found')
    
    def delete_begin(self):
        if self.head:
            self.head = self.head.ref
        else:
            raise Exception('LL is empty')
        
    def delete_end(self):
        curr = self.head
        if curr is None:
            raise Exception('LL is empty')
        prev = None
        while curr.ref:
            prev = curr
            curr = curr.ref
        if prev is None:
            self.head = None
        else:
            prev.ref = None

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.ref
            curr.ref = prev
            prev = curr
            curr = next_node
        self.head = prev

    def reverse_recursive(self):
        def _reverse(node, prev=None):
            if node is None:
                return prev
            next_node = node.ref
            node.ref = prev
            return _reverse(next_node, node)
        self.head = _reverse(self.head)

    def to_array(self):
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.ref
        return arr
    
    def from_array(self, array):
        if not array:
            return
        self.head = Node(array[0])
        node = self.head
        for i in array[1:]:
            node.ref = Node(i)
            node = node.ref

    def remove_dups(self):
        seen = set()
        curr = self.head
        prev = None
        while curr:
            if curr.val in seen:
                prev.ref = curr.ref
            else:
                seen.add(curr.val)
                prev = curr
            curr = curr.ref

    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.ref
        print("None")

    def display_reverse(self):
        def _reverse(node):
            if node is None:
                return
            _reverse(node.ref)
            print(node.val, end=' ->')
        _reverse(self.head)
        print()


if __name__ == "__main__":
    ll = LinkedList()

    print("=== Adding elements at beginning and end ===")
    ll.add_begin(10)
    ll.add_end(20)
    ll.add_end(30)
    ll.add_begin(5)
    ll.display()

    print("\n=== Add after 10 ===")
    ll.add_after(15, 10)
    ll.display()

    print("\n=== Add before 30 ===")
    ll.add_before(25, 30)
    ll.display()

    print("\n=== Delete begin ===")
    ll.delete_begin()
    ll.display()

    print("\n=== Delete end ===")
    ll.delete_end()
    ll.display()

    print("\n=== Convert to array ===")
    arr = ll.to_array()
    print(arr)

    print("\n=== Reverse Iterative ===")
    ll.reverse_iterative()
    ll.display()

    print("\n=== Reverse Recursive ===")
    ll.reverse_recursive()
    ll.display()

    print("\n=== Remove duplicates ===")
    ll.from_array([1, 2, 3, 2, 4, 1, 5])
    ll.display()
    ll.remove_dups()
    ll.display()

    print("\n=== Display Reverse ===")
    ll.display_reverse()

    print("\n=== Build from array ===")
    ll.from_array([100, 200, 300])
    ll.display()
    print("Array form:", ll.to_array())
