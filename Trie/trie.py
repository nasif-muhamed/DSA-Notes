from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        # checks if a word exists
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, word):
        # checks if a prefix exists
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word):
        # delete if word exists. Only change is_end = False if the node has other children else delete entire node.
        root = self.root

        def _delete_helper(node, word, idx):
            if idx == len(word):
                if not node.is_end:
                    return False  # Word doesn't exist
                node.is_end = False
                return len(node.children) == 0  # True if node can be deleted
            
            char = word[idx]
            if char not in node.children:
                return False  # Word doesn't exist
            
            can_delete_node = _delete_helper(node.children[char], word, idx + 1)
            if can_delete_node:
                del node.children[char]
                return len(node.children) == 0  # True if node can be deleted
            return False

        return _delete_helper(root, word, 0)

    # auto suggestions
    def find_words_with_prefix(self, prefix):
        # Step 1: Traverse to the end of the prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # Prefix not found
            node = node.children[char]
        
        def _helper(node, word, words):
            # If it's the end of a word, add it to the list
            if node.is_end:
                words.append(word)
            
            # Recursively collect words from each child
            for char, child_node in node.children.items():
                _helper(child_node, word + char, words)

        # Step 2: Collect all words starting from this node
        words = []
        _helper(node, prefix, words)
        return words
    
    # find smallest value
    def find_smallest_word(self):
        q = deque()
        q.append(("", self.root))

        while q:
            word, node = q.popleft()
            if node.is_end:
                return word
            for char in node.children:
                q.append((word+char, node.children[char]))

        
if __name__ == "__main__" :
    trie = Trie()

    # ✅ Insert words
    print("🔹 Inserting words...")
    words = ["man", "mango", "apple", "bat", "banana", "app"]
    for w in words:
        trie.insert(w)
    print("✅ Words inserted:", words)
    print()

    # 🔍 Search for words
    print("🔹 Testing search():")
    tests = ["man", "mango", "bat", "cat"]
    for t in tests:
        print(f"search('{t}') →", trie.search(t))
    print()

    # 🔎 Test starts_with()
    print("🔹 Testing starts_with():")
    prefixes = ["ma", "ban", "ap", "ca"]
    for p in prefixes:
        print(f"starts_with('{p}') →", trie.starts_with(p))
    print()

    # 💬 Test find_words_with_prefix()
    print("🔹 Testing find_words_with_prefix():")
    prefix_tests = ["ma", "ap", "b", "z"]
    for p in prefix_tests:
        print(f"Words with prefix '{p}':", trie.find_words_with_prefix(p))
    print()

    # ❌ Test delete()
    print("🔹 Testing delete():")
    print("Before delete 'mango' → search('mango') =", trie.search("mango"))
    trie.delete("mango")
    print("After delete 'mango' → search('mango') =", trie.search("mango"))
    print("Check prefix 'ma' after delete →", trie.find_words_with_prefix("ma"))
    print()

    # 🪶 Find smallest word (by length)
    print("🔹 Smallest word in Trie (by length):", trie.find_smallest_word())
