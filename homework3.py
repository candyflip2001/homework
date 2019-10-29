from collections import defaultdict
import sys

#Class to represent a graph for Kruscal's algorithm
class GraphForKruskalMST:

    def __init__(self, vertices): 
        self.V = vertices
        self.graph = []


    # Function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
  
    # Utility function to find set of an element i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Function that unions two sets of x and y
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Main function to construct MST using Kruskal's algorithm
    def KruskalMST(self):

        result = []

        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]

        self.graph = sorted(self.graph, key = lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

        # Pick the smallest edge and increment the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't cause cycle,
            # include it in result and increment the index
            # of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)  
            # Else discard the edge

        # Print the contents of result[] to display the built MST
        print ("Edge\tWeight")
        for u, v, weight in result:
            print ("%d -- %d\t  %d" % (u, v, weight))


#Class to represent a graph for Prim's algorithm
class GraphForPrimMST(): 
  
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def get_element(self, u, v):
        return self.gragh[u][v]
  
    # A utility function to print the constructed MST stored in parent[] 
    def printMST(self, parent): 
        print ("Edge\tWeight")
        for i in range(1, self.V): 
            print(parent[i], "--", i, "\t ", self.get_element(i, parent[i])) 

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Main function to construst and print MST using Prim's algorithm
    def primMST(self):

        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1 # First node is always the root of
  
        for i in range(self.V):

            u = self.minKey(key, mstSet)

            mstSet[u] = True

            # Update dist value of the adjacent vertices
            for v in range(self.V):
                if self.get_element(u, v) > 0 and mstSet[v] == False and key[v] > self.get_element(u, v):
                        key[v] = self.get_element(u, v)
                        parent[v] = u

        self.printMST(parent)




g = GraphForKruskalMST(8)

g.addEdge(0, 1, 10)
g.addEdge(0, 3, 10)
g.addEdge(0, 4, 5)
g.addEdge(1, 2, 8)
g.addEdge(1, 5, 5)
g.addEdge(2, 5, 4)
g.addEdge(2, 7, 1)
g.addEdge(3, 4, 10)
g.addEdge(3, 6, 10)
g.addEdge(4, 6, 5)
g.addEdge(4, 7, 9)
g.addEdge(5, 7, 3)
g.addEdge(6, 7, 8)

print("Kruskal's atgorithm:")
g.KruskalMST()
print("\n")

g = GraphForPrimMST(8)
g.gragh = [[ 0, 10,  0, 10,  5,  0,  0,  0],
           [10,  0,  8,  0,  0,  5,  0,  0],
           [ 0,  8,  0,  0,  0,  4,  0,  1],
           [10,  0,  0,  0, 10,  0, 10,  0],
           [ 5,  0,  0, 10,  0,  0,  5,  9],
           [ 0,  5,  4,  0,  0,  0,  0,  3],
           [ 0,  0,  0, 10,  5,  0,  0,  8],
           [ 0,  0,  1,  0,  9,  3,  8,  0]]

print("Prim's algorithm:")
g.primMST()
