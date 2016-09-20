# Karger's algorithm for finding min cuts of graphs
import random
import csv

def read_data():
    # read each row as a list, then store this list in a list of lists
    graph = []
    f = open('graph.txt')
    csv_f = csv.reader(f, delimiter='\t')
    for row in csv_f:
      graph.append(row)

    for sub_list in graph:
        for i in range(len(sub_list)):
            try:
                #convert to int
                sub_list[i] = int(sub_list[i])
            except:
                # remove the empty string
                sub_list.pop(i)
    return graph

def remove_self_loops():
    pass

def update_vertex_references():
    pass

def contract_random_points(graph):
    first_index = random.randint(0, len(graph))
    second_index = random.randint(0, len(graph[first_index]))




def karger(graph):
    while len(graph) > 2:
        old_vertex, new_vertex = contract_random_points(graph);
        update_vertex_references(old_vertex, new_vertex)
        remove_self_loops()
    print(graph)

def main():
    graph = read_data()
    print(graph)
    karger(graph)

if __name__ == '__main__':
    main()
