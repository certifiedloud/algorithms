"""
The file contains the edges of a directed graph. Vertices are labeled as positive
integers from 1 to 875714. Every row indicates an edge, the vertex label in first
column is the tail and the vertex label in second column is the head (recall the
graph is directed, and the edges are directed from the first column vertex to the
second column vertex). So for example, the 11th row looks liks : "2 47646".
This just means that the vertex with label 2 has an outgoing edge to the vertex
with label 47646

Your task is to code up the algorithm from the video lectures for computing
strongly connected components (SCCs), and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph,
in decreasing order of sizes, separated by commas (avoid any spaces). So if your
algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200
and 100, then your answer should be "500,400,300,200,100" (without the quotes).
If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms.
Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100,
then your answer should be "400,300,100,0,0" (without the quotes).
(Note also that your answer should not have any spaces in it.)
"""
from Node import Node

def read_data_in():
    print("Reading graph from file...")
    all_nodes = []
    graph = []
    for i in range(1, 875715):
        all_nodes.append(Node(i))
    with open("scc.txt") as f:
        current_node = all_nodes[0]
        for line in f:
            data, adjacent = line.split()
            print(data)
            if int(data) == current_node.data:
                current_node.neighbors.append(all_nodes[int(adjacent)])
            else:
                graph.append(current_node)
                current_node = all_nodes[int(data)]
                current_node.neighbors.append(all_nodes[int(adjacent)])
    del all_nodes
    print("Graph has been constructed!")


def main():
    read_data_in()

if __name__ == '__main__':
    main()
