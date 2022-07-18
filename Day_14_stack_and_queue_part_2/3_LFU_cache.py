'''
################## LFU Cache ##################
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

leetcode: https://leetcode.com/problems/lfu-cache/

'''

# This problem is difficult to explain here, best will be to watch the video https://www.youtube.com/watch?v=0PSB9y8ehbk&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=85



# solution
# Node class to implement Doubly linked list
class Node:
    def __init__(self, key, val, counter, prev=None, next_ = None):
        self.key = key
        self.val = val
        self.counter = counter
        self.prev = prev
        self.next = next_

# LRU cache class
class LRU:
    def __init__(self):
        self.head = Node(0,0,0)
        self.tail = Node(0,0,0)
        self.size = 0
        self.head.next, self.tail.prev = self.tail, self.head

    def insert(self, key, val, counter):
        temp = Node(key,val, counter)

        temp.next, temp.prev = self.head.next, self.head
        self.head.next, temp.next.prev = temp, temp

        self.size += 1
        return temp


    def deleteLRU(self):
        k = self.tail.prev.key
        self.delete(self.tail.prev)

        return k


    def delete(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        self.size -= 1


class LFUCache:

    def __init__(self, capacity: int):
        self.max_size = capacity
        self.fl = {}
        self.kv = {}
        self.freq = 0


    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1

        node = self.kv[key]
        freq = node.counter
        lru = self.fl[freq]

        value = node.val
        lru.delete(node)

        if lru.size == 0:
            if not self.freq < freq:
                self.freq = freq+1

        freq += 1

        if freq not in self.fl:
            self.fl[freq] = LRU()

        insertedNode = self.fl[freq].insert(key, value, freq)
        self.kv[key] = insertedNode

        return value


    def put(self, key: int, value: int) -> None:
        if key not in self.kv:
            if len(self.kv) < self.max_size:
                if 1 not in self.fl:
                    self.fl[1] = LRU()
                insetedNode = self.fl[1].insert(key, value, 1)
                self.kv[key] = insetedNode
                self.freq = 1

            else:
                if len(self.kv) == 0:
                    return
                lru = self.fl[self.freq]
                removedkey = lru.deleteLRU()
                del self.kv[removedkey]
                newFreq = 1


                if newFreq not in self.fl:
                    self.fl[newFreq] = LRU()

                insetedNode = self.fl[newFreq].insert(key, value, 1)
                self.kv[key] = insetedNode
                self.freq = 1

        else:
            node = self.kv[key]
            lru = self.fl[node.counter]
            f = node.counter
            lru.delete(node)
            newF = f + 1
            if lru.size == 0:
                if not self.freq < f:
                    self.freq = newF

            if newF not in self.fl:
                self.fl[newF] = LRU()
            insertedNode = self.fl[newF].insert(key, value, newF)
            self.kv[key] = insertedNode