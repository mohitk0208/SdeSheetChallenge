'''
########################## Cycle Detection in Directed Graph (DFS) ##########################
You are given a directed graph having ‘N’ nodes. A matrix ‘EDGES’ of size M x 2 is given which represents the ‘M’ edges such that there is an edge directed from node EDGES[i][0] to node EDGES[i][1].
Find whether the graph contains a cycle or not, return true if a cycle is present in the given directed graph else return false.

codestudio : https://www.codingninjas.com/codestudio/problems/1062626?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

'''


# cycle detection for directed graph is little different from undirected graph,
# in directed, we also need to if the node is visited in the current dfs call or not
# we do so by using another array called `dfsvis`

# solution
# SC -> O(n) + O(n) and TC -> O(n+e)
# Auxiliary space complexity (ASC) -> O(n)
def cycleDFS(node, vis, dfsvis, adj):
    vis[node] = True                # mark the node as visited
    dfsvis[node] = True             # mark the node as visited in the current dfs call

    for x in adj[node]:
        if not vis[x]:
            if cycleDFS(x, vis, dfsvis, adj):
                return True
        elif dfsvis[x] :      # if the node is visited and is also visited in the current dfs call then there is a cycle
            return True       # return true

    dfsvis[node] = False         # mark the node as not visited in the current dfs call, as the function is ending without
                                 # finding a cycle for the given node

    return False


def detectCycleInDirectedGraph(n, edges):
    vis = [False] * (n+1)                 # visited list
    dfsvis = [False] * (n+1)              # it contains the node which is visited in the current dfs call

    adj = [set([]) for _ in range(n+1)]
    for edge in edges:                    # create adjacency list
        adj[edge[0]].add(edge[1])

    for i in range(1, n+1):
        if not vis[i]:
            if cycleDFS(i, vis, dfsvis, adj):
                return True

    return False