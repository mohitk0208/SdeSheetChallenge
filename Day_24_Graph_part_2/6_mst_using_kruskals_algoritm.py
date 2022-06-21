'''
########################### MST using Kruskal's Algorithm ###########################
Given a weighted, undirected and connected graph of V vertices and E edges. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.
Since this is a functional problem you don't have to worry about input, you just have to complete the function  spanningTree() which takes number of vertices V and an adjacency matrix adj as input parameters and returns an integer denoting the sum of weights of the edges of the Minimum Spanning Tree. Here adj[i] contains a list of lists containing two integers where the first integer a[i][0] denotes that there is an edge between i and a[i][0] and second integer a[i][1] denotes that the distance between edge i and a[i][0] is a[i][1].

gfg : https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1#

'''


# approach : Kruskal's Algorithm
# SC -> O(E) + O(2N) and  TC -> O(ElogE)

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:

    ######### KRUSKAL'S ALGORITHM #################

    def spanningTree(self, V, adj):
        edges = []                                    # store all edges as (weight, u, v)

        for i in range(V):
            for x in adj[i]:
                edges.append((x[1], i, x[0]))

        edges.sort()                                  # sort edges by weight

        uf = UnionFind(V)                             # using disjoint set to find MST
        mstSum = 0                                    # store the sum of weights of MST
        for edge in edges:
            weight, u, v = edge

            if uf.connected(u, v):                    # check if nodes are already connected
                continue                              # if yes, skip this edge

            uf.union(u,v)                             # if not, connect them and add weight to MST
            mstSum += weight

        return mstSum