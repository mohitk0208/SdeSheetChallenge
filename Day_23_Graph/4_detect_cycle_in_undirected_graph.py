'''
################# Detect cycle in undirected graph #####################
You have been given an undirected graph with 'N' vertices and 'M' edges. The vertices are labelled from 1 to 'N'.
Your task is to find if the graph contains a cycle or not.
A path that starts from a given vertex and ends at the same vertex traversing the edges only once is called a cycle.

codestudio : https://www.codingninjas.com/codestudio/problems/1062670?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

'''

# solution
from queue import Queue

def cycleBFS(node, vis, adj):
    vis[node] = True
    q = Queue()
    q.put((node, -1))

    while len(q.queue) != 0:
        curr, par = q.get()

        for x in adj[curr]:
            if not vis[x]:
                vis[x] = True
                q.put((x, curr))
            elif x != par:              # if the node is visited and it is not the parent of the current node then
                return True             # it means it has been visited through some other path, hence a cycle exists, so return True

    return False    # if no cycle is found, return False



# code starts from this function
def cycleDetection(edges, n, m):
    # Return "Yes" if cycle id present in the graph else return "No".
    vis = [False] * (n+1)

    adj = [set([]) for _ in range(n+1)]   # adjacency list
    for edge in edges:                    # creating adjacency list from edges
        adj[edge[0]].add(edge[1])
        adj[edge[1]].add(edge[0])


    for i in range(1, n+1):             # checking for cycle in each node
        if not vis[i]:
            if cycleBFS(i, vis, adj):
                return "Yes"

    return "No"