"""
Compute Strongly Connected Components
Output: Size of 5 largest SCCs in the given graph
        decreasing order by size
"""
from collections import defaultdict

class Graph:
    """Representation of graph for SCC
        graph: dict of key: str, value: set of strs adjacencies
    """
    def __init__(self, n, graph=None):
        if graph is None: graph = defaultdict(list)
        self.__graph = graph
        self.__n = n

    def add_edge(self, v1, v2):
        self.__graph[v1].append(v2)

    def get_graph(self):
        return self.__graph

    def dfs_stack(self):
        """dfs on graph
        return stack of vertices by finishing time"""
        def dfs(i):
            """dfs from node i"""
            marked[i] = 1
            for j in self.__graph[i]:
                if not marked[j]:
                    dfs(j)
            stack.append(i)

        stack = []
        marked = [0] * self.__n

        for i in range(self.__n):
            if not marked[i]:
                dfs(i)

        return stack

    def reverse(self):
        """Reverse the graph edges"""
        new_g = defaultdict(list)
        for i in self.__graph.keys():
            for j in self.__graph[i]:
                new_g[j].append(i)
        self.__graph = new_g
        return new_g

    def dfs_2nd(self, i, marked, scc):
        marked[i] = 1
        scc.append(i)
        for j in self.__graph[i]:
            if not marked[j]:
                self.dfs_2nd(j, marked, scc)

    def scc(self):
        stack = self.dfs_stack()
        self.reverse()
        marked = [0] * self.__n
        while stack:
            i = stack.pop()
            if not marked[i]:
                scc = []
                self.dfs_2nd(i, marked, scc)
                print len(scc)


    def __str__(self):
        res = "Length: {}".format(len(self.__graph))
        return res



# def read_graph(filename):
#     """Read from file return dict"""
#     res = {}
#     with open(filename) as f:
#         lines = f.readlines()
#         for l in lines:
#             arr = l.split()
#             arr = map(int, arr)
#             res[arr[0]] = arr[1:]
#     return res
#
# if  __name__ == "__main__":
#     g = Graph(read_graph("./w4/SCC.txt"))
