'''
################## Bellman Ford Algorithm ##################
Given a weighted, directed and connected graph of V vertices and E edges, Find the shortest distance of all the vertex's from the source vertex S.
Note: The Graph doesn't contain any negative weight cycle.
Your Task:
You don't need to read input or print anything. Your task is to complete the function bellman_ford()  which takes number of vertices V and an E sized list of lists of three integers where the three integers are u,v, and w; denoting there's an edge from u to v, which has a weight of w as input parameters and returns a list of integers where the ith integer denotes the distance of ith node from source node. If some node isn't possible to visit, then it's distance should be 100000000(1e8

gfg : https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/0/?fbclid=IwAR2_lL0T84DnciLyzMTQuVTMBOi82nTWNLuXjUgahnrtBgkphKiYk6xcyJU

'''

'''
Bellman ford algorithm is used to find the shortest distance from a source vertex to all other vertices in a graph, even when the graph contains -ve edges, where the previous Dijkstra's algorithm fails.
Conditions for Bellman ford algorithm to work :
        1. The graph must be directed.
        2. The graph must not contain -ve cycles (i.e. sum of the cycle is -ve).

Uses  :
        1. To find the shortest path from a source vertex to all other vertices in a graph with -ve edges.
        2. To find if there is a negative weight cycle in a graph.

'''




# solution
# SC -> O(N) and TC -> O(N^2)

import math
class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: edges list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        dis = [100000000] * V                     # Initialize all distances as infinite (here 100000000)
        dis[S] = 0                                # Distance of source vertex from itself is always 0

        for _ in range(V-1):                      # Relax the edges exactly V-1 times

            for edge in edges:
                u, v, wt = edge

                if dis[u] == 100000000:
                    continue

                new_dis = dis[u] + wt
                if new_dis < dis[v]:              # Relax the edge if new distance is less than old distance
                    dis[v] = new_dis

        return dis                                # Return the distances array