'''
################### Is graph bipartite? (BFS) ###################
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

(DEFINITION OF BIPARTITE GRAPH)
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

leetcode : https://leetcode.com/problems/is-graph-bipartite/

'''

# (DEFINITION OF BIPARTITE GRAPH)
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

# it means that, for every edge connecting u and v,
# u ----- v
# u is in set A and v is in set B


# solution
# approach : BFS
from queue import Queue

class Solution:

    def bfsCheckBipartite(self, node, graph, vis, color):
        vis[node] = True                                    # mark node as visited
        color[node] = 1                                     # mark node as 1st color

        q = Queue()
        q.put(node)

        while len(q.queue) != 0:
            curr = q.get()
            c = 0 if color[curr] == 1 else 1          # color to be assigned to adjacent nodes of curr (opposite of curr's color)


            for x in graph[curr]:
                if not vis[x]:
                    vis[x] = True
                    color[x] = c
                    q.put(x)
                elif color[x] != color[curr]:             # if node is already visited and has same color as curr
                    return False                          # then graph is not bipartite, return False

        return True


    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)
        vis = [0]*n
        color = [-1] * n

        for i in range(n):
            if not vis[i]:
                if not self.bfsCheckBipartite(i, graph, vis, color):    # if not bipartite, return False
                    return False

        return True
