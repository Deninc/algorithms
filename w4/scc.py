"""
Compute Strongly Connected Components
Output: Size of 5 largest SCCs in the given graph
        decreasing order by size
"""
from collections import defaultdict

class Graph:
    """Representation of graph for SCC
        graph: dict of key: vertice, value: list of adjacencies
    """
    def __init__(self, n, graph=None):
        if graph is None: graph = defaultdict(list)
        self.__graph = graph
        self.__n = n

    def add_edge(self, v1, v2):
        """add an directed edge from v1 to v2"""
        self.__graph[v1].append(v2)

    def reverse(self):
        """Reverse the graph edges"""
        new_g = defaultdict(list)
        for i in self.__graph.keys():
            for j in self.__graph[i]:
                new_g[j].append(i)
        self.__graph = new_g

    def dfs_1st(self, v, marked, f):
        """dfs from node v"""
        stack = [(v, v), ]
        # instead of adding all neighbor of i to the stack
        # we add in the form of an edge (i, j)
        # before that we add (i, None) to indicate the backtracking
        # point of the node i -> finished
        while stack:
            i, j = stack.pop()
            if j is None:
                f.append(i)
            elif not marked[j]:
                marked[j] = 1
                stack.append((j, None))
                for k in self.__graph[j]:
                    if not marked[k]:
                        stack.append((j, k))

    def dfs_scc(self, v, marked):
        """dfs from v (leader)
        return size of this connected components"""
        size = 0
        stack = [v,]
        while stack:
            i = stack.pop()
            if not marked[i]:
                marked[i] = 1
                size += 1
                for j in self.__graph[i]:
                    stack.append(j)
        return size

    def scc(self):
        """the scc Algorithm"""
        print "First dfs"
        f = [] # finishing time stack
        marked = [0] * self.__n
        for v in range(self.__n):
            if not marked[v]:
                self.dfs_1st(v, marked, f)

        assert len(f) == self.__n
        print "Reversing"
        self.reverse()

        print "Second dfs"
        marked = [0] * self.__n
        sccs_size = []
        while f:
            i = f.pop()
            if not marked[i]:
                size = self.dfs_scc(i, marked)
                sccs_size.append(size)
        print "Return"

        return sorted(sccs_size, reverse=True)[:5]

if  __name__ == "__main__":
    print "Start reading"
    g = Graph(875715)
    with open("./w4/SCC.txt") as f:
        lines = f.readlines()
        for l in lines:
            arr = l.split()
            g.add_edge(int(arr[0]), int(arr[1]))
    print "Start processing"
    print g.scc()
