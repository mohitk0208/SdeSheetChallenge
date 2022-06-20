'''
################## Topological Sort (DFS) ##################
Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.

gfg: https://practice.geeksforgeeks.org/problems/topological-sort/1#
'''


# solution
class Solution:

    def dfs(self, node, adj, vis, ans):
        vis[node] = True

        for x in adj[node]:
            if not vis[x]:
                self.dfs(x, adj, vis, ans)

        ans.append(node)


#   Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        vis = [False] * V
        ans = []

        for i in range(V):
            if not vis[i]:
                self.dfs(i, adj, vis, ans)

        ans.reverse()

        return ans