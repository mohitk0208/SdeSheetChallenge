'''
####################### MST using Prim's Algorithm #######################
Given a weighted, undirected and connected graph of V vertices and E edges. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.

Since this is a functional problem you don't have to worry about input, you just have to complete the function  spanningTree() which takes number of vertices V and an adjacency matrix adj as input parameters and returns an integer denoting the sum of weights of the edges of the Minimum Spanning Tree. Here adj[i] contains a list of lists containing two integers where the first integer a[i][0] denotes that there is an edge between i and a[i][0] and second integer a[i][1] denotes that the distance between edge i and a[i][0] is a[i][1].

gfg : https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1#

'''

# MST Definition
# If we can draw a tree from a graph, consisting of N nodes and N-1 edges such that every node is reachable from every other node of the tree and total cost of edge weight in that tree is minimum, then the graph is called MST (Minimum Spanning Tree).


# solution

#Function to find sum of weights of edges of the Minimum Spanning Tree.
# -----------------------------------------------------------------------
######## Correct but not that efficient algorithm ####################
# SC -> O(3N) and TC -> more than O(N^2)
########################################################################
import math
class Solution:
    def spanningTree(self, V, adj):
        key = [math.inf]*V                            # key[i] stores the weight of the edge connecting node i to MST
        key[0] = 0                                    # initialize key[0] as 0 as 0 is the source

        mstSet = [False]*V                            # initialize mstSet as False as no node is in MST

        parent = [-1]*V                               # initialize parent as -1 as no node has parent yet

        for _ in range(V-1):                          # loop till V-1 edges are added to MST

            mini = math.inf
            min_idx = V+1

            for i in range(V):                           # find the index/node where key[i] is minimum and node is not in MST
                if mstSet[i] == False and key[i] < mini:
                    mini = key[i]
                    min_idx = i

            mstSet[min_idx] = True                       # add the node with min value to MST

            for x in adj[min_idx]:                        # iterate over all adjacent edges
                if mstSet[x[0]] == False and x[1] < key[x[0]]:  # if the node is not in MST and the weight of the edge is less
                    parent[x[0]] = min_idx                      # than its previous weight in key[] then update the parent
                    key[x[0]] = x[1]                            # update the key[] with the new weight

        return sum(key)                           # return the sum of weights of the edges in MST

##############################################################################






# approach 2 : use min heap to find the min weight edge that is not in MST
from heapq import heapify, heappush, heappop
import math

class Solution:


    # ##########Efficient Algorithm as min heap is used ##############
    # SC -> O(3N) and TC -> O(N + E + logN)
    def spanningTree(self, V, adj):
        key = [math.inf]*V
        key[0] = 0

        mstSet = [False] * V

        parent = [-1] * V

        pq = []                                                # initialize pq as min heap
        heapify(pq)                                            # store (weight, node) pairs in pq
        heappush(pq, (0, 0))                                   # add (0, 0) to pq, for 0 weight of 0th node

        count = 0                                              # count is the number of edges added to MST

        while count < V-1:
            min_idx = heappop(pq)[1]                           # pop the node with min weight from pq

            if mstSet[min_idx]:                                # if the node is already in MST then continue
                continue

            mstSet[min_idx] = True                            # add the node to MST
            count += 1                                        # increment the count of edges added to MST

            for x in adj[min_idx]:
                node = x[0]
                weight = x[1]
                if mstSet[node] == False and weight < key[node]:
                    parent[node] = min_idx
                    key[node] = weight
                    heappush(pq, (weight, node))              # add (weight, node) to pq


        return sum(key)