"""Dijkstra Shortest Path algorithm"""
from collections import defaultdict
import heapq

class Heap:
    """Min-Heap storing entry information supporting
    the Dijkstra shortest_path algorithm
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
    """Representation of graph for Shortest Path problem
        graph: dict of key: vertex, value: list of tuples (adj, length)
    """
    def __init__(self, n, graph=None):
        if graph is None: graph = defaultdict(list)
        self.__graph = defaultdict(list, graph)
        self.__n = n

    def add_edge(self, v1, v2, length):
        """add an weighted directed edge from v1 to v2"""
        self.__graph[v1].append((v2, length))

    def shortest_path(self, source):
        """dijkstra shortest_path from source vertex s"""
        marked = set()
        heap = Heap()
        heap.add_vertex(source, 0)  # from s to itself
        dist = defaultdict(int)
        dist[source] = 0
        while len(marked) < self.__n:
            vertex, distance = heap.pop_vertex()    # vertex and shortest dist
            marked.add(vertex)
            dist[vertex] = distance
            for tup in self.__graph[vertex]:
                adj, length = tup
                if adj not in marked:
                    new_dist = distance + length
                    if heap.contains(adj):
                        if new_dist < heap.get_weight(adj):
                            heap.add_vertex(adj, new_dist)
                    else:
                        heap.add_vertex(adj, new_dist)
        return dist

if __name__ == "__main__":
    g = Graph(200)
    with open("./w5/dijkstraData.txt") as f:
        lines = f.readlines()
        for l in lines:
            arr = l.split("\t")[:-1]    # last element is '\n'
            for adj in arr[1:]:
                v, w = adj.split(",")
                g.add_edge(int(arr[0]), int(v), int(w))
    dist = g.shortest_path(1)
    print dist[200]
