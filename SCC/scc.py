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
    existing_node_names = []
    current_data_name = 1
    all_nodes.append(Node(1))
    with open("scc.txt") as f:
        for line in f:
            v1, v2 = line.split(" ",1)
            v1 = int(v1)
            v2 = int(v2)
            if v1 > all_nodes[len(all_nodes)-1]:
                n1 = Node(v1)
                all_nodes.append(n1)
                if v2 not in n1.neighbors:
                    n2 = Node(v2)
                    n1.neighbors.append(n2)
            else:
                if v2 not in all_nodes:
                    n2 = Node(v2)
                    all_nodes.append(n2)
                all_nodes[len(all_nodes)-1].neighbors.append(n2)

    print(len(all_nodes))
    print(all_nodes)

def main():
    read_data_in()

if __name__ == '__main__':
    main()
