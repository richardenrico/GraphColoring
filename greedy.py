# A class to represent a graph object
class Graph:
 
    # Constructor
    def __init__(self, edges, N):
        self.adj = [[] for _ in range(N)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)
 
 
# Function to assign colors to vertices of a graph
def colorGraph(graph):
 
    # keep track of the color assigned to each vertex
    result = {}
 
    # assign a color to vertex one by one
    for u in range(N):
 
        # check colors of adjacent vertices of `u` and store them in a set
        assigned = set([result.get(i) for i in graph.adj[u] if i in result])

        # check for the first free color
        color = 1
        for c in assigned:
            if color != c:
                print("Color used in this graph :", c)
                break
            color = color + 1
 
        # assign vertex `u` the first available color
        result[u] = color
 
    for v in range(N):
        print("Color assigned to vertex", v, "is", colors[result[v]])
 
 
# Greedy coloring of a graph
if __name__ == '__main__':
 
    # Add more colors for graphs with many more vertices
    colors = ["", "BLUE", "GREEN", "RED", "YELLOW", "ORANGE", "PINK", 
                "BLACK", "BROWN", "WHITE", "PURPLE", "VOILET"]
 
    # of graph edges as per the above diagram
    edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
 
    # total number of nodes in the graph
    N = 6
 
    # build a graph from the given edges
    graph = Graph(edges, N)
 
    # color graph using the greedy algorithm
    colorGraph(graph)