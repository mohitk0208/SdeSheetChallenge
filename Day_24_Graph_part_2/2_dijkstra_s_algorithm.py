'''
########################## Dikstra's Algorithm ##########################
Given a weighted, undirected and connected graph of V vertices and E edges, Find the shortest distance of all the vertex's from the source vertex S.
Note: The Graph doesn't contain any negative weight cycle.

Your Task:
You don't need to read input or print anything. Your task is to complete the function dijkstra()  which takes the number of vertices V and an adjacency list adj as input parameters and returns a list of integers, where ith integer denotes the shortest distance of the ith node from the Source node. Here adj[i] contains a list of lists containing two integers where the first integer j denotes that there is an edge between i and j and the second integer w denotes that the weight between edge i and j is w.


gfg : https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1#

'''


# solution
from heapq import heapify, heappop, heappush
import math

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        pq = []                                             # minimum priority queue stores `(distance, node)`
        heapify(pq)                                         # and pops the minimum distance tuple.

        dis = [math.inf] * V                                # distance of each node from the source node.(initially infinity)
        dis[S] = 0                                          # distance of source node from itself is 0

        heappush(pq, (0, S))                                # push the source node to the queue

        while len(pq) != 0:
            curr = heappop(pq)                              # pop the minimum distance tuple

            for x in adj[curr[1]]:
                new_distance = dis[curr[1]] + x[1]          # new distance of the adjacent node from the source node

                if new_distance < dis[x[0]]:                # if new distance is less than the current distance
                    dis[x[0]] = new_distance                # update the distance of the adjacent node
                    heappush(pq, (new_distance, x[0]))      # and push it to the priority queue

        return dis                                          # return the distance of all the nodes from the source node