class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # insert a new value
    def insert(self, value):
        current_node = self.root
        if current_node is None:
            self.root = Node(value)
            return

        while True:
            if value < current_node.key:
                if current_node.left is None:
                    current_node.left = Node(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = Node(value)
                    break
                else:
                    current_node = current_node.right

    # check availability of a value
    def search(self, value):
        current_node = self.root
        while current_node is not None:
            if value < current_node.key:
                current_node = current_node.left
            elif value > current_node.key:
                current_node = current_node.right
            else:
                return True
        return False

    # remove a value - better to use recursion check AlternativeBST
    def remove(self, value, current=None, parent=None):
        if not self.root:
            return False
        if not current:
            current = self.root
        while current:
            if value < current.key:
                parent = current
                current = current.left
            elif value > current.key:
                parent = current
                current = current.right
            else:
                if current.left and current.right:
                    temp = self._min_value_node(current.right)
                    current.key = temp.key
                    self.remove(current.key, current.right, current)
                elif parent is None:
                    if current.left:
                        current.key = current.left.key
                        current.right = current.left.right
                        current.left = current.left.left
                    elif current.right:
                        current.key = current.right.key
                        current.right = current.right.right
                        current.left = current.right.left
                    else:
                        self.root = None
                elif current == parent.left:
                    parent.left = current.left if current.left else current.right
                elif current == parent.right:
                    parent.right = current.left if current.left else current.right
                break
        return self
    
    # find minimum value of a tree
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # In-order traversal: Left -> Root -> Right
    def inorder(self):
        def _inorder(root):
            if root:
                _inorder(root.left)
                print(root.key, end=' ')
                _inorder(root.right)
        _inorder(self.root)
        print()

    # Pre-order traversal: Root -> Left -> Right
    def preorder(self):
        def _preorder(root):
            if root:
                print(root.key, end=' ')
                _preorder(root.left)
                _preorder(root.right)
        _preorder(self.root)
        print()

    # Post-order traversal: Left -> Right -> Root
    def postorder(self):
        def _postorder(root):
            if root:
                _postorder(root.left)
                _postorder(root.right)
                print(root.key, end=' ')
        _postorder(self.root)
        print()

    # Level-order traversal
    def level_order(self):
        if not self.root:
            print('Empty Tree')
            return
        
        queue = [self.root]
        while queue:
            lvl_size = len(queue)
            for _ in range(lvl_size):
                node = queue.pop(0)
                print(node.key, end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()


# Alternative methods using recursion
class AlternativeBST(BST):
    # insert a new node
    def insert(self, new_key):     
        if self.root is None:
            self.root = Node(new_key)
        else:
            def _insert(node, new_key):
                if new_key < node.key:
                    if node.left is None:
                        node.left = Node(new_key)
                    else:
                        _insert(node.left, new_key)

                else:
                    if node.right is None:
                        node.right = Node(new_key)
                    else:
                        _insert(node.right, new_key)
            _insert(self.root, new_key)

    # check availability of a value
    def search(self, key):
        def _search(node, key):
            if node is None:
                return False
            elif key < node.key:
                return _search(node.left, key)
            elif key > node.key:
                return _search(node.right, key)
            else:
                return True
        return _search(self.root, key)

    # remove a value - easy to learn than using while loop
    def delete(self, key):
        def _delete_recursively(node, key):
            if node is None:
                return node

            if key < node.key:
                node.left = _delete_recursively(node.left, key)
            elif key > node.key:
                node.right = _delete_recursively(node.right, key)
            else:
                # Node with only one child or no child
                if node.left is None:
                    return node.right

                elif node.right is None:
                    return node.left

                # Node with two children: Get the inorder successor (smallest in the right subtree)
                temp = self._min_value_node(node.right)
                node.key = temp.key
                node.right = _delete_recursively(node.right, temp.key)

            return node

        self.root = _delete_recursively(self.root, key)

    # find minimum value of a tree
    def _min_value_node(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            return self._min_value_node(node.left)
        return node


class AdvancedBST(AlternativeBST):
    # find height of a tree: counting edges - from Node to leaf
    def find_height(self, node):
        if node is None:
            return -1 # or 0 if counting nodes
        left = self.find_height(node.left)
        right = self.find_height(node.right)
        return 1 + max(left, right)

    # find depth of a tree: counting edges - from root to Node
    def find_depth(self, root, node, depth=0):
        if root is None:
            return -1
        elif root == node:
            return depth
        elif node.key < root.key:
            return self.find_depth(root.left, node, depth+1)
        else:
            return self.find_depth(root.right, node, depth+1)
        
    # find Kth smallest element (for Kth largest, change the inorder node.left to right and vice versa)
    def find_kth_smallest(self, k):
        self.result = None
        self.count = 0
        def inorder(node):
            if node and self.result is None:
                inorder(node.left)
                self.count += 1
                if self.count == k:
                    self.result = node.key
                    return
                inorder(node.right)

        inorder(self.root)
        return self.result
    
    # find 2nd smallest element (for 2nd largest change the left to right)
    def find_second_smallest(self):
        if not self.root or (not self.root.left and not self.root.right):
            return None
        
        parent = None
        curr = self.root
        while curr.left:
            parent = curr
            curr = curr.left

        if curr.right:
            curr = curr.right
            while curr.left:
                curr = curr.left
            return curr.val
        
        return parent.val if parent else None
    
    # checks perfect tree or not
    def is_perfect_tree(self):
        h = self.find_height(self.root) + 1  # adjust for edge-based height
        def is_perfect(node, height, level=1):
            if not node:
                return True
            
            # Leaf node
            if not node.left and not node.right:
                return height == level
            
            # Internal node must have both children
            if not node.left or not node.right:
                return False
            
            # Recurse for both subtrees
            return (is_perfect(node.left, height, level+1) and
                    is_perfect(node.right, height, level+1))
        return is_perfect(self.root, h)

    # checks balanced tree or not
    def is_balanced(self, node):
        if node is None:
            return True

        left_height = self.find_height(node.left)
        right_height = self.find_height(node.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.is_balanced(node.left) and self.is_balanced(node.right)

    # find the nearest value available to a target
    def find_closest_value(self, target):
        current = self.root
        closest = current.key

        while current:
            # Update closest if current node is closer to the target
            if abs(current.key - target) < abs(closest - target):
                closest = current.key

            # Move left or right in the tree depending on the target value
            if target < current.key:
                current = current.left
            elif target > current.key:
                current = current.right
            else:
                # If we find the exact target, we can return it
                return f"Closest Value to {target} is {current.key}"

        return f"Closest Value to {target} is {closest}"

    # check a tree is BST or not.
    @staticmethod
    def is_bst(node, min_val=None, max_val=None):
        if not node:
            return True

        # Check if the current node's value is within the allowed range
        if ((min_val is not None and node.key < min_val) or
                (max_val is not None and node.key > max_val)):
            return False

        # Validate left and right subtrees with updated bounds
        return (AdvancedBST.validate(node.left, min_val, node.key) and
                AdvancedBST.validate(node.right, node.key, max_val))



if __name__ == '__main__':
    bst = AdvancedBST()
    print(bst.search(100))
    bst.insert(100)
    bst.insert(50)
    bst.insert(150)
    bst.insert(25)
    bst.insert(75)
    bst.insert(125)
    bst.insert(175)
    print('Is BST:', bst.validate(bst.root))
    bst.inorder()
    bst.preorder()
    bst.postorder()
    print(bst.find_closest_value(0))
    print(bst.search(125))
    print(bst.search(1111))
    print('Is BST:', bst.is_bst(bst.root))

    bst.delete(175)
    print('-----------------')
    bst.inorder()
    print("Level Order:")
    bst.level_order()

