import time
import numpy as np
import multiprocessing
from multiprocessing import Pipe, Lock

ADJ_MATRIX_FILE = 'graph1.txt'

class Graph:
    def __init__(self, adj_mat):
        self.adj_mat = adj_mat
        self.create_nodes(self.calc_degrees())
        self.connect_nodes()

    def create_nodes(self, degrees):
        node_ids = set([i for i in range(len(self.adj_mat[0]))])
        self.V = [Node(i, degrees[i]) for i in node_ids]

    def calc_degrees(self):
        return multiprocessing.Pool().map(self.calc_degree, range(len(self.adj_mat[0])))
    
    def calc_degree(self, vertex):
        return sum(self.adj_mat[vertex])
    
    def connect_nodes(self):
        for i in range(len(self.adj_mat[0])):
            self.connect_node(self.V[i])

    def connect_node(self, node):
        neighbour_indexes = np.nonzero(self.adj_mat[node.id])[0]
        for i in range(len(neighbour_indexes)):
            node.connect(self.V[neighbour_indexes[i]])


class Node:
    def __init__(self, id, degree):
        self.id = id
        self.MIS = False
        self.used = False
        self.degree = degree
        self.neighbours = {}

    def set_neighbour(self, neighbour_id, pipe):
        if not neighbour_id in self.neighbours:
            self.neighbours[neighbour_id] = pipe
            return True
        return False

    def connect(self, node):
        conn1, conn2 = Pipe()
        if node.set_neighbour(self.id, input):
            self.set_neighbour(node.id, conn1)
        

def string_to_matrix(source):
    lines = source.split('\n')
    return [list(map(int, line.split(','))) for line in lines]

def read_file(file):
    with open(file) as f: s = f.read()
    return s

def get_adj_matrix():
    s = read_file(ADJ_MATRIX_FILE)
    return string_to_matrix(s)

def preporcess():
    graph = Graph(get_adj_matrix())
    return graph

def slowMIS(graph):
    
    return


def main():
    print("Preprocessing...")
    start_time = time.time()
    graph = preporcess()
    mid_time = time.time()
    print("Preprocessing finished in %s seconds!" % (mid_time - start_time))
    print("Calculating MIS...")
    slowMIS(graph)
    end_time = time.time()
    print("Calculating MIS finished in %s seconds!" % (end_time - mid_time))
    print("--- Total execution: %s seconds ---" % (end_time - start_time))


if __name__ == "__main__":
    main()
