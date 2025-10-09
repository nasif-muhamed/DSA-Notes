class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    # Pre-order traversal: Root -> Left -> Right
    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # In-order traversal: Left -> Root -> Right
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # Post-order traversal: Left -> Right -> Root
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    # Level-order traversal
    def level_order(self):
        if not self.root:
            return

        queue = [self.root]
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                print(node.value, end=" ")

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()

    # Insert: incase of "complete" binary tree.
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)

            if not node.left:
                node.left = new_node
                return
            else:
                queue.append(node.left)

            if not node.right:
                node.right = new_node
                return
            else:
                queue.append(node.right)

    # sum of Tree
    def tree_sum(self):
        def _tree_sum(node):
            if node is None:
                return 0
            return node.value + _tree_sum(node.left) + _tree_sum(node.right)
        return _tree_sum(self.root)
    
    # sum of left nodes of a Tree
    def tree_left_sum(self, node):
        if node is None:
            return 0
        
        total = 0
        if node.left:
            total += node.left.value

        total += self.tree_left_sum(node.left)
        total += self.tree_left_sum(node.right)
        return total

    # count of leaf nodes
    def leaf_count(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1
        
        return self.leaf_count(node.left) + self.leaf_count(node.right)

    # sum of leaf nodes
    def leaf_sum(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return node.value
        
        return self.leaf_sum(node.left) + self.leaf_sum(node.right)

    # checking identical or not
    @staticmethod
    def is_identical(node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.value != node2.value:
            return False
        return BinaryTree.is_identical(node1.left, node2.left) and BinaryTree.is_identical(node1.right, node2.right)
        

    # checking symmetric or not
    @staticmethod
    def is_symmetric(node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.value != node2.value:
            return False
        return BinaryTree.is_symmetric(node1.left, node2.right) and BinaryTree.is_symmetric(node1.right, node2.left)
    

    # checking subtree or not
    @staticmethod
    def is_subtree(parent_root, child_root):
        if child_root is None:
            return True
        if parent_root is None:
            return False
        
        # Either - exact subtree - from same tree
        if parent_root is child_root:
            return True
        
        # Or - incase of nodes from separate trees
        # if BinaryTree.is_identical(parent_root, child_root):
        #     return True
        return BinaryTree.is_subtree(parent_root.left, child_root) or BinaryTree.is_subtree(parent_root.right, child_root)
        

if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(-4)
    tree.insert(-5)

    print("Level-order traversal:")
    tree.level_order()  # Output: 1 2 3 4 5
    print('Sum:', tree.tree_sum())
    print('Left sum:', tree.tree_left_sum(tree.root))
    print('Leaf count:', tree.leaf_count(tree.root))
    print('Leaf sum:', tree.leaf_sum(tree.root))
    print('Is sub tree?:', tree.is_subtree(tree.root, tree.root.right.right))

    tree1 = BinaryTree(1)
    tree1.insert(2)
    tree1.insert(2)
    tree1.insert(3)
    tree1.insert(4)
    tree1.insert(3)
    tree1.insert(4)
    print('Is identical?:', tree1.is_identical(tree1.root.left, tree1.root.right))
    print('Is symmetric?:', tree1.is_symmetric(tree1.root.left, tree1.root.right))

    tree2 = BinaryTree(1)
    tree2.insert(2)
    tree2.insert(2)
    tree2.insert(3)
    tree2.insert(4)
    tree2.insert(4)
    tree2.insert(3)
    print('Is identical?:', tree2.is_identical(tree2.root.left, tree2.root.right))
    print('Is symmetric?:', tree2.is_symmetric(tree2.root.left, tree2.root.right))
