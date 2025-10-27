class Node:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_begin(self, val):
        new_node = Node(val, None, self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def add_end(self, val):
        new_node = Node(val, self.tail, None)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def add_after(self, val, after):
        curr = self.head
        while curr:
            if curr.val == after:
                new_node = Node(val, curr, curr.next)
                if curr.next:
                    curr.next.prev = new_node
                else:
                    self.tail = new_node
                curr.next = new_node
                return
            curr = curr.next
        raise Exception("Target not found")

    def add_before(self, val, before):
        curr = self.head
        while curr:
            if curr.val == before:
                new_node = Node(val, curr.prev, curr)
                if curr.prev:
                    curr.prev.next = new_node
                else:
                    self.head = new_node
                curr.prev = new_node
                return
            curr = curr.next
        raise Exception("Target not found")

    def delete_begin(self):
        if self.head is None:
            raise Exception("DLL is empty")
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = self.tail = None

    def delete_end(self):
        if self.tail is None:
            raise Exception("DLL is empty")
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = self.tail = None

    def display_forward(self):
        curr = self.head
        while curr:
            print(curr.val, end=" <-> ")
            curr = curr.next
        print("None")

    def display_backward(self):
        curr = self.tail
        while curr:
            print(curr.val, end=" <-> ")
            curr = curr.prev
        print("None")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.add_begin(10)
    dll.add_end(20)
    dll.add_end(30)
    dll.add_begin(5)
    dll.display_forward()

    dll.add_after(15, 10)
    dll.add_before(25, 30)
    dll.display_forward()

    dll.delete_begin()
    dll.delete_end()
    dll.display_forward()

    print("Backward Display:")
    dll.display_backward()
