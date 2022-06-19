'''
##################### BFS #####################
Given a directed graph. The task is to do Breadth First Traversal of this graph starting from 0.
Note: One can move from node u to node v only if there's an edge from u to v and find the BFS traversal of the graph starting from the 0th vertex, from left to right according to the graph. Also, you should only take nodes directly or indirectly connected from Node 0 in consideration.
Your task:
You don’t need to read input or print anything. Your task is to complete the function bfsOfGraph() which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns  a list containing the BFS traversal of the graph starting from the 0th vertex from left to right.

gfg : https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1#

'''

# solution
# SC -> O(n) + O(n) and TC -> O(n)
from queue import Queue

class Solution:

    def bfs(self, i, vis, adj, ans):
        ans.append(i)
        vis[i] = True

        q = Queue()
        q.put(i)

        while len(q.queue) != 0:
            x = q.get()

            for y in adj[x]:
                if not vis[y]:
                    vis[y] = True
                    ans.append(y)
                    q.put(y)




    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        ans = []
        vis = [False]*V

        self.bfs(0, vis, adj, ans)

        return ans