'''
################## DFS #######################
Given a connected undirected graph. Perform a Depth First Traversal of the graph.
Note: Use recursive approach to find the DFS traversal of the graph starting from the 0th vertex from left to right according to the graph..

gfg : https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
'''

# solution
# gfg solution
# SC -> O(n) + O(n) and TC -> O(n)
class Solution:

    def dfs(self, i, vis, adj, ans):
        ans.append(i)
        vis[i] = True

        for x in adj[i]:
            if not vis[x]:
                self.dfs(x, vis, adj, ans)

    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        ans = []

        vis = [False] * V

        for i in range(V):
            if not vis[i]:
                self.dfs(i, vis, adj, ans)

        return ans