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

def merge_vertices(first_vertex, second_vertex, first_sub_list, graph):
    # find the second list and add it to the first, then remove the original
    # first_list = first_index
    second_sub_list = 0
    for i in range(0,len(graph)):
        if graph[i][0] == second_vertex:
            second_sub_list = i
    orig_sec_list = graph[second_sub_list]
    # remove the duplicate vertex
    try:
        graph[second_sub_list].remove(first_vertex)
    except:
        pass
    # combine the two lists
    graph[first_sub_list] = graph[first_sub_list] + graph[second_sub_list]

    # clean up other references to the old vertex
    for i in range(len(graph)):
        # for j in range(len(graph[i])):
        for item in graph[i][1:]:
            if item == second_vertex:
                graph[i].remove(item)

    graph.remove(graph[second_sub_list])
    #remove_self_loops(graph)

def remove_self_loops(graph):
    for i in range(len(graph)):
        for item in graph[i]:
            if item == graph[i][0]:
                graph[i].remove(item)
def contract_random_points(graph):
    print(len(graph))
    first_sub_list = random.randint(0, len(graph)-1)
    first_vertex = graph[first_sub_list][0]
    second_vertex = graph[first_sub_list][random.randint(1, len(graph[first_sub_list])-1)]

    print("\
     first_vertex: {}\n\
     second_vertex: {}\n\
     ".format(first_vertex, second_vertex))

    merge_vertices(first_vertex, second_vertex, first_sub_list, graph)

def karger(graph):
    while len(graph) > 2:
        contract_random_points(graph);

def main():
    graph = read_data()
    karger(graph)
    print(graph, len(graph))

if __name__ == '__main__':
    main()
