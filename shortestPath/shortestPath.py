
class Vertex:
    def __init__(self, name):
        # The node name
        self.name = name

        # A list of tuples in the form (neighborNode, edgeDistance)
        self.neighbors = []

        def __str__(self):
            return self.name

all_vertices = []
discovered_vertices = []
distances = []
with open("graph.txt") as f:
    for line in f:
        parts = line.split()
        first_vertex = Vertex(int(parts[0]))
        for neighbor in parts[1:]:
            vertex, distance = neighbor.split(",")
            first_vertex.neighbors.append((int(vertex), int(distance)))

        all_vertices.append(first_vertex)

# Initialize first distance 0
distances.append(0)
while len(all_vertices) is not 0:
    v = all_vertices.pop()
    print(v.name, v.neighbors)
