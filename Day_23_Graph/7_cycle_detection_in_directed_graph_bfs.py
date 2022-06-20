'''
####################### Cycle Detection in Directed Graph (BFS) ##########################
You are given a directed graph having ‘N’ nodes. A matrix ‘EDGES’ of size M x 2 is given which represents the ‘M’ edges such that there is an edge directed from node EDGES[i][0] to node EDGES[i][1].
Find whether the graph contains a cycle or not, return true if a cycle is present in the given directed graph else return false.

codestudio : https://www.codingninjas.com/codestudio/problems/1062626?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

'''


# solution using Topological Sort (BFS) OR Kahn's algorithm
from queue import Queue

def detectCycleInDirectedGraph(n, edges):

    adj = [set([]) for _ in range(n+1)]   # adjacency list
    for edge in edges:
        adj[edge[0]].add(edge[1])


    q = Queue()                      # queue for order of nodes
    in_degree = [0] * (n+1)          # in_degree(number of incoming edges) of each node


    for i in range(1, n+1):
        for x in adj[i]:            # increment in_degree of all nodes adjacent to i
            in_degree[x] += 1


    for x in range(1, n+1):         # start with the nodes that have in_degree 0
        if in_degree[x] == 0:
            q.put(x)


    count = 0                       # it stores the number of nodes that have been inserted in the queue
    ans = []                        # stores the topological order of the nodes

    # Actual Algorithm
    while len(q.queue) != 0:      # while the queue is not empty
        curr = q.get()
        count += 1
        ans.append(curr)          # store the current node in the ans

        for x in adj[curr]:     # decrement the in_degree of all nodes adjacent to curr
            in_degree[x] -= 1
            if in_degree[x] == 0: # if the in_degree of a node becomes 0, add it to the queue
                q.put(x)

    if count == n: return False
    return True