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
    second_sub_list = 0
    for i in range(0,len(graph)):
        if graph[i][0] == second_vertex:
            second_sub_list = i

    # remove the duplicate vertex
    try:
        graph[second_sub_list].remove(first_vertex)
    except:
        pass
    # combine the two lists
    graph[first_sub_list] = graph[first_sub_list] + graph[second_sub_list]

    # clean up other references to the old vertex
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == second_vertex:
                graph[i][j] = first_vertex

    graph.remove(graph[second_sub_list])
    remove_self_loops(graph)

def remove_self_loops(graph):
    for i in range(len(graph)):
        for item in graph[i][1:]:
            if item == graph[i][0]:
                graph[i].remove(item)
def contract_random_points(graph):
    print(len(graph))
    first_sub_list = random.randint(0, len(graph)-1)
    first_vertex = graph[first_sub_list][0]
    if len(graph[first_sub_list])>1:
        second_vertex = graph[first_sub_list][random.randint(1, len(graph[first_sub_list])-1)]
    else:
        pass

    print("\
     first_vertex: {}\n\
     second_vertex: {}\n\
     ".format(first_vertex, second_vertex))

    merge_vertices(first_vertex, second_vertex, first_sub_list, graph)

def karger(graph):
    while len(graph) > 2:
        contract_random_points(graph);

def main():
    # possible_mins = []
    # for i in range(1000):
    #     random.seed()
    #     graph = read_data()
    #     karger(graph)
    #     min = -1
    #     firstLen = len(graph[0])
    #     secondLen = len(graph[1])
    #     min = firstLen + secondLen
    #     possible_mins.append(min)
    # print("possible mins", sorted(possible_mins))
    graph = read_data()
    karger(graph)
    print(graph, len(graph[0]), len(graph[1]))

if __name__ == '__main__':
    main()
