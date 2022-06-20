'''
########################## Course Schedule ##########################
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


leetcode : https://leetcode.com/problems/course-schedule/

'''


'''

logic here to solve problem is, consider each prerequisite as an edge showing a dependency,
if there is a cycle in the graph then, there is no way to finish all the courses as each course is dependent on each other.
on the other hand, if there is no cycle in the graph, then all courses can be finished.

'''


# solution
# approach : BFS
from queue import Queue

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses

        adj = [[] for _ in range(n)]
        for p in prerequisites:
            adj[p[0]].append(p[1])


        q = Queue()
        in_degree = [0]*n
        for i in range(n):
            for x in adj[i]:
                in_degree[x] += 1

        for i in range(n):
            if in_degree[i] == 0:
                q.put(i)


        count = 0

        while len(q.queue) != 0:
            curr = q.get()
            count += 1

            for x in adj[curr]:
                in_degree[x] -= 1
                if in_degree[x] == 0:
                    q.put(x)

        # count == n means no cycle, so course can be completed
        if count == n: return True

        return False




# approach 2 : DFS
class Solution:

    def checkCycleDFS(self, node, adj, vis, dfsvis):
        vis[node] = True
        dfsvis[node] = True

        for x in adj[node]:
            if not vis[x]:
                if self.checkCycleDFS(x, adj, vis, dfsvis):
                    return True
            elif dfsvis[x]:
                    return True

        dfsvis[node] = False

        return False


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        vis = [False] * n
        dfsvis = [False] * n
        adj = [[] for _ in range(n)]
        for p in prerequisites:
            adj[p[0]].append(p[1])

        for i in range(n):
            if not vis[i]:
                if self.checkCycleDFS(i, adj, vis, dfsvis):
                    return False

        return True
