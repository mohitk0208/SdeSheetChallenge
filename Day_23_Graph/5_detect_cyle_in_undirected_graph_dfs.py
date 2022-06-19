'''
########################### Detect Cycle in undirected graph DFS ##########################
You have been given an undirected graph with 'N' vertices and 'M' edges. The vertices are labelled from 1 to 'N'.
Your task is to find if the graph contains a cycle or not.
A path that starts from a given vertex and ends at the same vertex traversing the edges only once is called a cycle.

codestudio : https://www.codingninjas.com/codestudio/problems/1062670?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

'''


# solution
def cycleDFS(node, parent, vis, adj):
    vis[node] = True                # mark the node as visited

    for x in adj[node]:
        if not vis[x]:
            if cycleDFS(x, node, vis, adj): # check for cycle in the child node, if exists, then return True
                return True
        elif x != parent :              # if the node is visited and it is not the parent of the current node then
            return True                 # it means it has been visited through some other path, hence a cycle exists, so return True

    return False



def cycleDetection(edges, n, m):
    # Return "Yes" if cycle id present in the graph else return "No".
    vis = [False] * (n+1)

    adj = [set([]) for _ in range(n+1)]
    for edge in edges:
        adj[edge[0]].add(edge[1])
        adj[edge[1]].add(edge[0])


    for i in range(1, n+1):
        if not vis[i]:
            if cycleDFS(i, -1, vis, adj):
                return "Yes"

    return "No"