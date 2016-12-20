from collections import defaultdict

class DisjointSet():
    """Support Union/Find"""

    def __init__(self, n):
        """id: list of vertices
        * note: assuming vertices are numbered between 1 to n
        size[i]: number of vertices in the tree root i
        count: number of disjoint sets (tree)
        """
        self.__id = [x for x in range(0, n+1)] # abandon the key 0
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
    """graph: dict of key: vertex, value: list of tuples (adj, length)
    """
    def __init__(self, n, graph_dict=None):
        if graph_dict is None: graph_dict = {}
        self.__graph = graph_dict
        self.__edges = self.__generate_edges()
        self.__n = n

    def __generate_edges(self):
        """return list of tuple (v1, v2, length)
        where exists an edge connects between v1 and v2 (no duplicates)
        """
        edges = []
        for v in self.__graph:
            for vi in self.__graph[v]:
                if v < vi[0]:
                    edges.append((v, vi[0], vi[1]))
        return edges

    def clustering(self, k):
        """repeatedly merge closet pair of separated points (spacing)
        until there're only k clusters left
        return the final spacing
        """
        edges = sorted(self.__edges, key=lambda x: x[2])
        clusters = DisjointSet(self.__n)
        i = 0
        while len(clusters) > k:
            # find closet pair of points
            v1, v2, _ = edges[i]
            # if v1, v2 might be in the same cluster / not separated
            # the union will be terminated anyway
            clusters.union(v1, v2)
            i += 1

        return edges[i][2]

# if __name__ == "__main__":
#     d = defaultdict(list)
#     with open("w8/clustering1.txt") as f:
#         l = f.readlines()
#
#     n = int(l[0])
#     for edge in l[1:]:
#         v1, v2, l = edge.split()
#         d[int(v1)].append((int(v2), int(l)))
#
#     g = Graph(n, d)
#     space = g.clustering(3)
#     assert space == 3203, "%s is Incorrect!" % space
#     print "Correct!"
