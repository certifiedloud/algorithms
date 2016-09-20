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

def remove_self_loops(graph):
    pass

def merge_vertices(first_vertex, second_vertex, first_sub_list, graph):
    # find the second list and add it to the first, then remove the original
    # first_list = first_index
    second_sub_list = 0
    for i in range(0,len(graph)):
        if graph[i][0] == second_vertex:
            second_sub_list = i
    graph[first_sub_list] = graph[first_sub_list] + graph[second_sub_list]

    # clean up the newly extended first list
    print(graph[first_sub_list])
    print(graph[second_sub_list])
    print("trying to remove ", first_vertex)
    try:
        graph[1:first_sub_list].remove(first_vertex)
    except:
        # do nothing
        pass

    # clean up other references to the old vertex
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == second_vertex:
                del graph[i][j]

    graph.remove(graph[second_sub_list])



def contract_random_points(graph):
    first_sub_list = random.randint(0, len(graph)-1)
    first_vertex = graph[first_sub_list][0]
    print
    second_vertex = random.randint(1, len(graph[first_sub_list])-1)
    # second_index = random.randint(1, len(graph[first_index])-1)

    # first_vertex = graph[first_index][0]
    print("----- ", first_vertex)
    # second_vertex = graph[first_index][second_index]

    print("\
     first_vertex: {}\n\
     second_vertex: {}\n\
     ".format(first_vertex, second_vertex))

    merge_vertices(first_vertex, second_vertex, first_sub_list, graph)
    remove_self_loops(graph)

    return 1,2



def karger(graph):
    # while len(graph) > 2:
    old_vertex, new_vertex = contract_random_points(graph);
    #print(graph)

def main():
    graph = read_data()
    #print(graph)
    karger(graph)

if __name__ == '__main__':
    main()
