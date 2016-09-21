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


    # remove_self_loops(graph)
    indices_to_remove = []
    # print("the len ",len(graph[first_sub_list]))
    for i in range(1, len(graph[first_sub_list])):
        if graph[first_sub_list][i] == first_vertex:
            indices_to_remove.append(i)

    # reverse sort these indices so we can remove them in a loop without conflicts
    sorted(indices_to_remove)
    indices_to_remove.reverse()
    for i in indices_to_remove:
        del graph[first_sub_list][i]

    # remove old list that was merged
    graph.remove(graph[second_sub_list])

def contract_random_points(graph):
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
    possible_mins = []
    for i in range(100):
        random.seed()
        graph = read_data()
        karger(graph)
        min = -1
        firstLen = len(graph[0])
        secondLen = len(graph[1])
        min = firstLen
        possible_mins.append(min-1) #subtract one to account for the node label
    print("possible mins", sorted(possible_mins))
    print(graph)

if __name__ == '__main__':
    main()
