import random
import math

"""
CLASSES
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

    def __generate_edges(self):
        """return set of frozensets of two values (v1, v2)
        where exists an edge connects between v1 and v2
        """
        edges = []
        for v in self.__graph:
            for vi in self.__graph[v]:
                if v < vi:
                    edges.append((v, vi))
        return edges

    def __cut(self):
        """return a random cut of Graph g"""
        cut = DisjointSet(len(self.__graph))
        random.shuffle(self.__edges)
        i = 0
        while len(cut) > 2:
            e = self.__edges[i]
            i += 1
            v1, v2 = e
            cut.union(v1, v2)

        # exercise: no. of crossed edges
        count = 0
        for e in self.__edges[i:]:
            v1, v2 = e
            if cut.root(v1) != cut.root(v2):
                count += 1
        return count

    def min_cut(self):
        """cut n^2*log(n) times to get min cut"""
        n = len(self.__graph)
        N = int((n**2) * math.log(n))
        min_cut = self.__cut()
        for _ in range(N):
            cut = self.__cut()
            if cut < min_cut: min_cut = cut
        return min_cut

    def __str__(self):
        res = "Vertices: "
        res += " ".join(map(str, self.__graph.keys()))
        res += "\nEdges: "
        for s in self.__edges:
            res += "-".join(map(str, list(s)))
            res += " "
        return res

"""
MAIN
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
    g = Graph(read_graph("./w3/kargerMinCut.txt"))
    print g.min_cut()
