# Tree with any number of nodes
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def add_child(self, parent_node, value):
        child_node = Node(value)
        parent_node.children.append(child_node)
        return child_node
    
    def find(self, value):
        def _find(node, value):
            if node is None:
                return None
            
            if node.value == value:
                return node
            
            for child in node.children:
                found = _find(child, value)
                if found:
                    return found
            
            return None

        return _find(self.root, value)
    
    def display(self):
        def _display(node, level):
            print(" " * (level * 2) + f"- {node.value}")
            for child in node.children:
                _display(child, level + 1)
        
        if self.root: 
            _display(self.root, level=0)
        else:
            print("Tree is empty")


if __name__ == "__main__":
    print('------Tree------')
    tree = Tree("Root")
    a = tree.add_child(tree.root, "A")
    b = tree.add_child(tree.root, "B")
    tree.add_child(a, "A1")
    tree.add_child(a, "A2")
    tree.add_child(b, "B1")
    tree.add_child(b, "B2")

    tree.display()

    found = tree.find("A2")
    print("\nFound:", found.value if found else "Not found")


# Complete Ternary Tree:
# - Tree with Three Nodes 
# - All level Except last level should be completed. Should be completed from left to right in the last level.
class TernaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = [None] * 3


class TernaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TernaryTreeNode(value)
        if self.root is None:
            self.root = new_node
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            for idx, child in enumerate(node.children):
                if child is None:
                    node.children[idx] = new_node
                    return
                queue.append(child)

    def search(self, value):
        def _search(node, value):
            if node is None:
                return None
            
            if node.value == value:
                return node
            
            for child in node.children:
                found = _search(child, value)
                if found is not None:
                    return found
                
            return None
        return _search(self.root, value)

    def level_order(self):
        if self.root is None:
            print('Tree is empty')
            return
        
        queue = [self.root]
        while queue:
            lvl_size = len(queue)
            for _ in range(lvl_size):
                node = queue.pop(0)
                print(node.value, end=' ')
                for child in node.children:
                    if child is not None:
                        queue.append(child)
            print()


if __name__ == "__main__":
    print('------Ternary Tree------')
    tree = TernaryTree()
    tree.insert("A")
    tree.insert("B")
    tree.insert("C")
    tree.insert("D")
    tree.insert("E")
    tree.insert("F")

    found = tree.search("F")
    print("Found:", found.value if found else "Not found")

    print("Level Order:")
    tree.level_order()
