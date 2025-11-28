"""
Order of operations matters
Linked list pointers represent the structure.
The map represents quick access.

Insight
Always first fix the structure (unlink or move nodes in the linked list).
Then update the hash map.
"""

class Node:
    def __init__(self, key, value, prevn=None, nextn=None):
        self.key = key
        self.value = value
        self.prevn = prevn
        self.nextn = nextn

    def __repr__(self):
        return f"Node(key={self.key}, value={self.value})"


class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.map = {}  # key -> Node
        self.capacity = capacity

        # sentinels: last ... first
        self.last = Node(0, 0)  # LRU sentinel (left)
        self.first = Node(0, 0)  # MRU sentinel (right)
        self.last.nextn = self.first
        self.first.prevn = self.last

    def _remove(self, node: Node) -> None:
        """Unlink node from the doubly-linked list."""
        node.prevn.nextn = node.nextn
        node.nextn.prevn = node.prevn
        node.prevn = node.nextn = None  # optional

    def _add_to_mru(self, node: Node) -> None:
        """Insert node right before `first` sentinel (most-recent position)."""
        node.prevn = self.first.prevn
        node.nextn = self.first
        self.first.prevn.nextn = node
        self.first.prevn = node

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if node is None:
            return -1
        # move to MRU
        self._remove(node)
        self._add_to_mru(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            # move existing node to MRU
            self._remove(node)
            self._add_to_mru(node)
            return

        # evict if needed
        if len(self.map) >= self.capacity:
            lru = self.last.nextn
            self._remove(lru)
            del self.map[lru.key]

        # insert new node at MRU
        new_node = Node(key, value)
        self.map[key] = new_node
        self._add_to_mru(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
