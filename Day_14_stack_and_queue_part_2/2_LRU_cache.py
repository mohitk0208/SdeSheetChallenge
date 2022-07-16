'''
######################## LRU Cache (Important) #########################
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

-> LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
-> int get(int key) Return the value of the key if the key exists, otherwise return -1.
-> void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.

If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.


leetcode : https://leetcode.com/problems/lru-cache/

'''


# solution
# DS USED =  doubly linked list, hash map(dict)

# node class for doubly linked list
class Node:
    def __init__(self, key, value, prev=None, next_=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next_


class LRUCache:

    # initialize the cache with capacity
    def __init__(self, capacity: int):
        self.size = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.c = {}
        self.head.next, self.tail.prev = self.tail, self.head

    # get the value of the key if the key exists, otherwise return -1
    # SC -> O(1) and TC -> O(1)
    def get(self, key: int) -> int:
        if key not in self.c:
            return -1

        val = self.c[key].value
        self.delete(self.c[key])
        self.insert(key, val)

        return val

    # SC -> O(1) and TC -> O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.c:
            self.delete(self.c[key])
            self.insert(key, value)
            return

        if len(self.c) < self.size:
            self.insert(key, value)
            return


        self.deleteLRU()
        self.insert(key, value)


    def deleteLRU(self):
        self.delete(self.tail.prev)


    def delete(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        del self.c[node.key]


    def insert(self, key, val):
        temp = Node(key, val)
        temp.next, temp.prev = self.head.next, self.head
        self.head.next, temp.next.prev = temp, temp

        self.c[key] = temp