class Node:
    def __init__(self, val, ref=None):
        self.val = val
        self.ref = ref


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self, val):
        new_node = Node(val)
        if self.head is None:
            new_node.ref = new_node
            self.head = new_node
            return
        curr = self.head
        while curr.ref != self.head:
            curr = curr.ref
        curr.ref = new_node
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, val):
        new_node = Node(val)
        if self.head is None:
            new_node.ref = new_node
            self.head = new_node
            return
        curr = self.head
        while curr.ref != self.head:
            curr = curr.ref
        curr.ref = new_node
        new_node.ref = self.head

    def delete_begin(self):
        if self.head is None:
            raise Exception("CLL is empty")
        if self.head.ref == self.head:
            self.head = None
            return
        curr = self.head
        while curr.ref != self.head:
            curr = curr.ref
        curr.ref = self.head.ref
        self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            raise Exception("CLL is empty")
        if self.head.ref == self.head:
            self.head = None
            return
        curr = self.head
        prev = None
        while curr.ref != self.head:
            prev = curr
            curr = curr.ref
        prev.ref = self.head

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        curr = self.head
        while True:
            print(curr.val, end=" -> ")
            curr = curr.ref
            if curr == self.head:
                break
        print("(back to head)")


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.add_end(10)
    cll.add_end(20)
    cll.add_end(30)
    cll.display()

    print("\nAdd at beginning:")
    cll.add_begin(5)
    cll.display()

    print("\nDelete from beginning:")
    cll.delete_begin()
    cll.display()

    print("\nDelete from end:")
    cll.delete_end()
    cll.display()


class Node:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self, val):
        new_node = Node(val)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = new_node
            return
        tail = self.head.prev
        new_node.next = self.head
        new_node.prev = tail
        tail.next = new_node
        self.head.prev = new_node
        self.head = new_node

    def add_end(self, val):
        new_node = Node(val)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = new_node
            return
        tail = self.head.prev
        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node

    def delete_begin(self):
        if self.head is None:
            raise Exception("CDLL is empty")
        if self.head.next == self.head:
            self.head = None
            return
        tail = self.head.prev
        self.head = self.head.next
        self.head.prev = tail
        tail.next = self.head

    def delete_end(self):
        if self.head is None:
            raise Exception("CDLL is empty")
        if self.head.next == self.head:
            self.head = None
            return
        tail = self.head.prev
        new_tail = tail.prev
        new_tail.next = self.head
        self.head.prev = new_tail

    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return
        curr = self.head
        while True:
            print(curr.val, end=" <-> ")
            curr = curr.next
            if curr == self.head:
                break
        print("(back to head)")

    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return
        curr = self.head.prev
        while True:
            print(curr.val, end=" <-> ")
            curr = curr.prev
            if curr.next == self.head:
                break
        print("(back to head)")


if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()

    print("=== Add elements at beginning and end ===")
    cdll.add_begin(10)
    cdll.add_end(20)
    cdll.add_end(30)
    cdll.add_begin(5)
    cdll.display_forward()

    print("\n=== Delete from beginning ===")
    cdll.delete_begin()
    cdll.display_forward()

    print("\n=== Delete from end ===")
    cdll.delete_end()
    cdll.display_forward()

    print("\n=== Display backward ===")
    cdll.display_backward()
