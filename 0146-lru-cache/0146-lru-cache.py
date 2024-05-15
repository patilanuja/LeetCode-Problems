class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to node (key, val) # so val will be present in nodes

        ## intialize left and right node
        # left will point to least recently used key
        # right will point to most recently used key
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # remove from any end 
    def remove(self, node):
        ## n1 n2 n3 #remove n2
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev 

    # add at the right end 
    def insert(self, node):
        ## n1   n3 # insert n2
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt


    def get(self, key: int) -> int:
        # check if key exist in cache
        # if yes, return update its position(remove the node from it original position and put it at the last position)
        # if no, return -1
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1        
        

    def put(self, key: int, value: int) -> None:
        # check if key exist in cache
        # if yes, update it position
        # if not, create new node with given key and values and insert the key into the cache 
        # check the capacity of the cache 
        # if cache is bigger than given capacity, remove the lru key
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove lru
            lru = self.left.next
            # remove function removes value from LinkedList
            self.remove(lru)
            # del delets it from cache map
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)