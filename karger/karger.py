# Karger's algorithm for finding min cuts of graphs
import random
import csv

def read_data():
    # read each row as a list, then store this list in a list of lists
    graph = []
    f = open('graph.txt')
    csv_f = csv.reader(f, delimiter='\t')
    for row in csv_f:
      graph.append(row[1:len(row)-1])
    return graph


def karger():
    # contract two random points

    # delete self-loops
    pass

def main():
    graph = read_data()
    print(graph[199])
    karger()

if __name__ == '__main__':
    main()
