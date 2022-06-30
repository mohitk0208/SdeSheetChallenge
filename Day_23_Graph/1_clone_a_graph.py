'''
################## Clone a graph ###################
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


leetcode : https://leetcode.com/problems/clone-graph/

'''


# solution


# SC -> O(n) and TC -> O(n)
from queue import Queue
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None

        nodes = {}

        q = Queue()                           # queue to implement BFS
        vis = set([])                         # visited nodes
        q.put(node)
        vis.add(node)                         # add the first node to visited nodes

        while len(q.queue) != 0:   # do BFS and create a new node for each node in the graph
            x = q.get()
            temp = Node(x.val)
            nodes[x] = temp

            for neighbor in x.neighbors:
                if neighbor not in vis:
                    vis.add(neighbor)
                    q.put(neighbor)

        vis = set([])
        vis.add(node)
        q.put(node)

        # Deeep copy the graph
        while len(q.queue) != 0:       # Now do a BFS again to connect the nodes in the graph
            x = q.get()
            s = nodes[x]

            s.neighbors = [nodes[key] for key in x.neighbors]
            for neighbor in x.neighbors:
                if neighbor not in vis:
                    vis.add(neighbor)
                    q.put(neighbor)

        return nodes[node]                # return the first node in the new graph