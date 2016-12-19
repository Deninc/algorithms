"""
Minimum Spanning Tree problem
"""

from collections import defaultdict
import heapq

class Heap:
    """Min-Heap with delete function
    """

    REMOVED = "<removed vertex>"    # placeholder for removed entry

    def __init__(self):
        """ entry = (weight, vertex)
            weight = greedy score from source to this vertex"""
        self.__heap = []
        self.__entries = {}    # mapping of vertex to its entry

    def contains(self, vertex):
        """if heap contains this vertex"""
        return self.__entries.has_key(vertex)

    def get_weight(self, vertex):
        """get current weight of vertex in the heap entry"""
        return self.__entries[vertex][0]

    def add_vertex(self, vertex, weight):
        """add new entry to heap or update weight of vertex"""
        if vertex in self.__entries:
            self.remove_vertex(vertex)
        entry = [weight, vertex]
        self.__entries[vertex] = entry
        heapq.heappush(self.__heap, entry)

    def remove_vertex(self, vertex):
        """mark an entry as removed"""
        entry = self.__entries.pop(vertex)
        entry[-1] = Heap.REMOVED

    def pop_vertex(self):
        """get the entry with min weight"""
        while self.__heap:
            weight, vertex = heapq.heappop(self.__heap)
            if vertex != Heap.REMOVED:
                del self.__entries[vertex]
                return vertex, weight
        raise KeyError("empty heap")


class Graph:
    """Representation of graph for MST problem
        graph: dict of key: vertex, value: list of tuples (adj, length)
    """
    def __init__(self, n, graph=None):
        if graph is None: graph = defaultdict(list)
        self.__graph = defaultdict(list, graph)
        self.__n = n

    def add_edge(self, v1, v2, length):
        """add an weighted directed edge from v1 to v2"""
        self.__graph[v1].append((v2, length))

    def mst(self):
        """compute minimum spanning tree"""
        marked = set()
        heap = Heap()
        heap.add_vertex(1, 0)   # should be random instead of vertex 1
        # T = set() # MST: set of edges in tree
        overall_cost = 0    # cost of all edges in MST

        while len(marked) < self.__n:
            vertex, distance = heap.pop_vertex()
            marked.add(vertex)
            overall_cost += distance # add the edge length
            for edge in self.__graph[vertex]:
                adj, length = edge
                if adj not in marked:
                    if heap.contains(adj):
                        if length < heap.get_weight(adj):
                            heap.add_vertex(adj, length)
                    else:
                        heap.add_vertex(adj, length)

        return overall_cost

# if __name__ == "__main__":
#     with open("w7/edges.txt") as f:
#         l = f.readlines()
#
#     n = int(l[0].split()[0])
#     g = Graph(n)
#     for edge in l[1:]:
#         v1, v2, length = edge.split()
#         g.add_edge(int(v1), int(v2), int(length))
#
#     print g.mst()
