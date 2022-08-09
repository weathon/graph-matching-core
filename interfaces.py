from graph_pkg_core.algorithm.graph_edit_distance import GED
from graph_pkg_core.edit_cost.edit_cost_vector import EditCostVector
from graph_pkg_core.graph.edge import Edge
from graph_pkg_core.graph.graph import Graph
from graph_pkg_core.graph.label.label_edge import LabelEdge
from graph_pkg_core.graph.label.label_node_vector import LabelNodeVector
from graph_pkg_core.graph.node import Node
from graph_pkg_core.loader.loader_vector import LoaderVector

import numpy as np
import os

graph_list = {}
ged = GED(EditCostVector(1., 1., 1., 1., 'euclidean'))
def load_graph(path):
    global graph_list
    lists = os.listdir(path)
    for i in lists:
        with open(path + i, 'r') as f:
            lines = f.readlines()
            n = int(lines[0].split(" ")[1])
            tmp = Graph(i,i,n)

            for nL in lines[1:]:
                nL = nL.split(" ")
                if nL[0] == 'v':
                    tmp.add_node(Node(int(nL[1]), LabelNodeVector(np.array([float(nL[2])]))))
                else:
                    tmp.add_edge(Edge(int(nL[1]), int(nL[2]), LabelEdge(float(nL[3])))) #float
            graph_list[int(lines[0].split(" ")[2])]=tmp

def GED(name1, name2):
    return ged.compute_edit_distance(graph_list[name1], graph_list[name2])


if __name__ == "__main__":
    load_graph("../dataForReal/")
    print(GED(179, 180))