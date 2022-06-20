'''
################### Is graph bipartite? (DFS) ###################
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
# approach : DFS
class Solution:

    def dfsCheckBipartite(self, node, c,  vis, graph, color):
        vis[node] = True
        color[node] = c                 # set the color of node to c

        for x in graph[node]:
            next_c = 0 if color[node] == 1 else 1
            if not vis[x]:
                if not self.dfsCheckBipartite(x, next_c, vis, graph, color):
                    return False
            elif color[x] == color[node]: # if color of node is same as color of adjacent node, return false
                return False

        return True


    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)
        vis = [0]*n
        color = [-1] * n

        for i in range(n):
            if not vis[i]:
                if not self.dfsCheckBipartite(i, 1, vis, graph, color) :
                    return False

        return True