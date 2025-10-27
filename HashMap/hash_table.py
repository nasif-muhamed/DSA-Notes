# Basic Implementation
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        # Check if key exists, update it
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise, add new key-value pair
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for idx, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][idx]
                return True
        return False

    def show(self):
        result = []
        for arr in self.table:
            chain = []
            for key, value in arr:
                chain.append(f"{key} : {value}")
            result.extend(chain)
        print(result)

    def __str__(self):
        return str(self.table)


if __name__ == '__main__':
    ht = HashTable()
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("orange", 30)
    ht.insert("apple", 50)   # update existing
    print(ht)                # shows internal structure
    ht.show()
    print(ht.get("apple"))   # 50
    ht.delete('orange')
    print(ht)                # shows internal structure


# Collision Handling & rehashing/resizing
# 1. Seperate Chaining / Open Hashing: with linked list - above one is also separarte chaining.
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTableLL:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size
        self.count = 0
        self.load_factor = 0.7

    def _hash(self, key):
        return hash(key) % self.size
        
    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0

        for node in old_table:
            if node is not None:
                while node:
                    self.insert(node.key, node.value)
                    node = node.next

    def insert(self, key, value):
        index = self._hash(key)
        head = self.table[index]

        if head is None:
            self.table[index] = Node(key, value)
            self.count += 1
            return

        # Traverse linked list to check if key exists
        curr = head
        while curr:
            if curr.key == key:
                curr.value = value
                return
            if curr.next is None:
                break
            curr = curr.next

        # Add new node at end of chain
        curr.next = Node(key, value)
        self.count += 1
        
        if (self.count / self.size) > self.load_factor:
            self._resize()

    def get(self, key):
        index = self._hash(key)
        curr = self.table[index]

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return None  # Not found

    def delete(self, key):
        index = self._hash(key)
        curr = self.table[index]
        prev = None

        while curr:
            if curr.key == key:
                if prev is None:
                    self.table[index] = None
                else:
                    prev.next = curr.next
                self.count -= 1
                return
            prev = curr
            curr = curr.next

        return False
    
    def __str__(self):
        result = []
        for i, node in enumerate(self.table):
            chain = []
            curr = node
            while curr:
                chain.append(f"{curr.key}:{curr.value}")
                curr = curr.next
            result.append(f"{i}: " + " -> ".join(chain))
        return "\n".join(result)


if __name__ == '__main__':
    ht = HashTableLL()
    ht.insert("apple", 5)
    ht.insert("banana", 10)
    ht.insert("guva", 15)
    ht.insert("apple", 7)  # update
    print(ht.get("apple"))  # 7
    print(ht)
    ht.delete("banana")


# 2. Open Addressing / Closed Hashing:
# a. Linear Probing:
class HashTableLinearProbing:
    def __init__(self, initial_size=8):
        self.size = initial_size
        self.count = 0
        self.table = [None] * self.size
        self.load_factor_threshold = 0.7

    def _hash(self, key):
        return hash(key) % self.size

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0  # reset and reinsert everything

        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])  # reinsert old key-value pairs

    def insert(self, key, value):
        if self.count / self.size >= self.load_factor_threshold:
            self._resize()

        index = self._hash(key)
        for i in range(self.size):
            probe_index = (index + i) % self.size
            if self.table[probe_index] is None or self.table[probe_index][0] == key:
                if self.table[probe_index] is None:
                    self.count += 1
                self.table[probe_index] = (key, value)
                return
        raise Exception("Hash Table is Full")

    def get(self, key):
        index = self._hash(key)
        for i in range(self.size):
            probe_index = (index + i) % self.size
            if self.table[probe_index] is None:
                return None
            if self.table[probe_index][0] == key:
                return self.table[probe_index][1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i in range(self.size):
            probe_index = (index + i) % self.size
            if self.table[probe_index] is None:
                return False
            if self.table[probe_index][0] == key:
                self.table[probe_index] = None
                self.count -= 1
                return True
        return False

    def __str__(self):
        return str(self.table)


if __name__ == '__main__':
    ht = HashTableLinearProbing()
    for i in range(20):  # triggers resize
        ht.insert(f"key{i}", i)
    print(ht)


# b. Quadratic Probing
class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash(key)
        i = 0
        while self.table[(index + i**2) % self.size] is not None:
            if self.table[(index + i**2) % self.size][0] == key:
                self.table[(index + i**2) % self.size] = (key, value)
                return
            i += 1
            if i == self.size:
                raise Exception("Hash Table Full")
        self.table[(index + i**2) % self.size] = (key, value)

    def search(self, key):
        index = self._hash(key)
        i = 0
        while self.table[(index + i**2) % self.size] is not None:
            if self.table[(index + i**2) % self.size][0] == key:
                return self.table[(index + i**2) % self.size][1]
            i += 1
            if i == self.size:
                break
        return None


# c. Double Hashing
class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.prime = self._get_prime_less_than(size) 
        # we can use a constant pre detarmained value, less than the length. instead of the complex function. But prime number is best for avoiding cycles.

    def _get_prime_less_than(self, n):
        for num in range(n-1, 1, -1):
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    break
            else:
                return num
        return 3

    def _hash1(self, key):
        return key % self.size

    def _hash2(self, key):
        return self.prime - (key % self.prime)

    def insert(self, key, value):
        index = self._hash1(key)
        step = self._hash2(key)
        i = 0
        while self.table[(index + i * step) % self.size] is not None:
            if self.table[(index + i * step) % self.size][0] == key:
                self.table[(index + i * step) % self.size] = (key, value)
                return
            i += 1
            if i == self.size:
                raise Exception("Hash Table Full")
        self.table[(index + i * step) % self.size] = (key, value)

    def search(self, key):
        index = self._hash1(key)
        step = self._hash2(key)
        i = 0
        while self.table[(index + i * step) % self.size] is not None:
            if self.table[(index + i * step) % self.size][0] == key:
                return self.table[(index + i * step) % self.size][1]
            i += 1
            if i == self.size:
                break
        return None


# using same syntax as python dictionary:
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of buckets

    def _hash(self, key):
        """Compute hash index for a key."""
        return hash(key) % self.size

    def __setitem__(self, key, value):
        """Insert or update a key-value pair."""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                # update existing key
                bucket[i] = (key, value)
                return
        # add new key-value pair
        bucket.append((key, value))

    def __getitem__(self, key):
        """Retrieve value for a key."""
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def __delitem__(self, key):
        """Delete a key-value pair."""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(key)

    def __repr__(self):
        """For nice printing."""
        pairs = [f"{k!r}: {v!r}" for bucket in self.table for k, v in bucket]
        return "{" + ", ".join(pairs) + "}"


if __name__ == '__main__':
    table = HashTable()

    table['name'] = 'Alice'
    table['age'] = 25

    print(table['name'])   # → Alice
    print(table['age'])    # → 25

    table['age'] = 26      # update
    print(table)           # → {'name': 'Alice', 'age': 26}

    del table['name']
    print(table)           # → {'age': 26}


# Easy Implementations. Has to double check before replacing above.
# linear probing
class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.load_factor = 0.7
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size
    
    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        
        for pair in old_table:
            if pair is not None:
                self.insert(**pair)

    def insert(self, key, value):
        idx = self._hash(key)

        for i in range(self.size):
            new_idx = (idx + i) % self.size
            if self.table[new_idx] is None or self.table[new_idx][0] == key:
                if self.table[new_idx] is None:
                    self.count += 1
                self.table[new_idx] = (key, value)
                break
        else:
            raise Exception('Table is full')
        
        if (self.count / self.size) > self.load_factor:
            self._resize()

    def get(self, key):
        idx = self._hash(key)

        for i in range(self.size):
            new_idx = (idx + i) % self.size
            if self.table[new_idx] is None:
                return Exception('No key found')
            if self.table[new_idx][0] == key:
                return self.table[new_idx][1]
        else:
            raise Exception('No key found')
        
    def delete(self, key):
        idx = self._hash(key)

        for i in range(self.size):
            new_idx = (idx + i) % self.size
            if self.table[new_idx] is None:
                return Exception('No key found')
            if self.table[new_idx][0] == key:
                self.table[new_idx] = None
                self.count -= 1
                return
        else:
            raise Exception('No key found')


class HashTableQuadratic:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.load_factor = 0.7
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0

        for pair in old_table:
            if pair is not None:
                self.insert(*pair)  # unpack (key, value)

    def insert(self, key, value):
        idx = self._hash(key)

        for i in range(self.size):
            new_idx = (idx + i * i) % self.size  # 👈 quadratic probing
            if self.table[new_idx] is None or self.table[new_idx][0] == key:
                if self.table[new_idx] is None:
                    self.count += 1
                self.table[new_idx] = (key, value)
                break
        else:
            raise Exception('Table is full')

        if (self.count / self.size) > self.load_factor:
            self._resize()

    def get(self, key):
        idx = self._hash(key)

        for i in range(self.size):
            new_idx = (idx + i * i) % self.size  # 👈 quadratic probing
            if self.table[new_idx] is None:
                raise Exception('No key found')
            if self.table[new_idx][0] == key:
                return self.table[new_idx][1]
        else:
            raise Exception('No key found')

    def delete(self, key):
        idx = self._hash(key)

        for i in range(self.size):
            new_idx = (idx + i * i) % self.size  # 👈 quadratic probing
            if self.table[new_idx] is None:
                raise Exception('No key found')
            if self.table[new_idx][0] == key:
                self.table[new_idx] = None
                self.count -= 1
                return
        else:
            raise Exception('No key found')


class HashTableDoubleHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.load_factor = 0.7
        self.count = 0

    def _hash1(self, key):
        """Primary hash function"""
        return hash(key) % self.size

    def _hash2(self, key):
        """Secondary hash function (must be non-zero and < size)"""
        # A common choice is to use a smaller prime
        return 1 + (hash(key) % (self.size - 1))

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0

        for pair in old_table:
            if pair is not None:
                self.insert(*pair)

    def insert(self, key, value):
        idx1 = self._hash1(key)
        idx2 = self._hash2(key)

        for i in range(self.size):
            new_idx = (idx1 + i * idx2) % self.size  # 👈 double hashing
            if self.table[new_idx] is None or self.table[new_idx][0] == key:
                if self.table[new_idx] is None:
                    self.count += 1
                self.table[new_idx] = (key, value)
                break
        else:
            raise Exception("Table is full")

        if (self.count / self.size) > self.load_factor:
            self._resize()

    def get(self, key):
        idx1 = self._hash1(key)
        idx2 = self._hash2(key)

        for i in range(self.size):
            new_idx = (idx1 + i * idx2) % self.size
            if self.table[new_idx] is None:
                raise Exception("No key found")
            if self.table[new_idx][0] == key:
                return self.table[new_idx][1]
        else:
            raise Exception("No key found")

    def delete(self, key):
        idx1 = self._hash1(key)
        idx2 = self._hash2(key)

        for i in range(self.size):
            new_idx = (idx1 + i * idx2) % self.size
            if self.table[new_idx] is None:
                raise Exception("No key found")
            if self.table[new_idx][0] == key:
                self.table[new_idx] = None
                self.count -= 1
                return
        else:
            raise Exception("No key found")
