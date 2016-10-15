import random
import math

"""
Classes: Graph, UnionFind...
"""

class DisjointSet():
    """Representation of merged vertices when performing min cut algorithm
    """
    def __init__(self, n):
        """id: list of vertices
        * note: assuming vertices are numbered between 1 to n
        size[i]: number of vertices in the tree root i
        count: number of disjoint set (tree)
        """
        self.__id = [x for x in range(0, n+1)]
        self.__size = [1 for _ in range(n)] # for weighted union
        self.__count = n

    def __len__(self):
        return self.__count

    def root(self, i):
        """find root of the set contains i
        also performing path compression while searching"""
        while self.__id[i] != i:
            self.__id[i] = self.__id[self.__id[i]] # path compression
            i = self.__id[i]
        return i

    def union(self, v1, v2):
        """ weighted quick-union
        """
        i = self.root(v1)
        j = self.root(v2)

        if i == j: return

        if self.__size[i-1] < self.__size[j-1]:
            self.__id[i] = j
            self.__size[j-1] += self.__size[i-1]
        else:
            self.__id[j] = i
            self.__size[i-1] += self.__size[j-1]

        self.__count -= 1

class Graph:
    """Representation of graph for min cut problem
        graph: dict of key: str, value: set of strs adjacencies
    """
    def __init__(self, graph_dict=None):
        if graph_dict is None: graph_dict = {}
        self.__graph = graph_dict
        self.__edges = self.__generate_edges()

    def __len__(self):
        return len(self.__graph)

    def __generate_edges(self):
        edges = set()
        for v in self.__graph:
            for vi in self.__graph[v]:
                if frozenset([v, vi]) not in edges:
                    edges.add(frozenset([v, vi]))
        return edges

    def min_cut(self):
        """return mincut of Graph g"""
        cut = DisjointSet(len(self.__graph))
        edges = self.__edges.copy()
        while len(cut) > 2:
            e = random.choice(tuple(edges))
            edges.discard(e)
            v1, v2 = e
            cut.union(v1, v2)
        # no. of crossed edges
        count = 0
        for e in edges:
            v1, v2 = e
            if cut.root(v1) != cut.root(v2):
                count += 1
        return count

    def __str__(self):
        res = "Vertices: "
        res += " ".join(map(str, self.__graph.keys()))
        res += "\nEdges: "
        for s in self.__edges:
            res += "-".join(map(str, list(s)))
            res += " "
        return res

"""
Read from file
"""
def read_graph(filename):
    """Read from file return dict"""
    res = {}
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            arr = l.split()
            arr = map(int, arr)
            res[arr[0]] = arr[1:]
    return res

if  __name__ == "__main__":
    g = Graph(read_graph("kargerMincut.txt"))
    n = len(g)
    N = int((n**2) * math.log(n))
    min_cut = g.min_cut()
    for _ in range(N):
        cut = g.min_cut()
        if cut < min_cut: min_cut = cut
    print min_cut
