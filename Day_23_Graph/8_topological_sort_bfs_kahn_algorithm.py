'''
#################### Topological Sort (BFS) (Kahn's Algorithm) ####################
Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph

'''

# Kahn's Algorithm

# solution
# SC -> O(n) + O(n) + O(n) and TC -> O(n+e)
from queue import Queue

class Solution:

    def topoSort(self, V, adj):
        q = Queue()
        in_degree = [0] * V

        for i in range(V):
            for x in adj[i]:
                in_degree[x] += 1

        for i in range(V):
            if in_degree[i] == 0:
                q.put(i)

        ans = []

        while len(q.queue) != 0:
            curr = q.get()
            ans.append(curr)

            for x in adj[curr]:
                in_degree[x] -= 1
                if in_degree[x] == 0:
                    q.put(x)

        return ans
