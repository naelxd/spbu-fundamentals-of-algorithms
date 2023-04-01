from typing import Any
from queue import PriorityQueue

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from src.plotting import plot_graph


def prim_mst(G: nx.Graph, start_node="0") -> set[tuple[Any, Any]]:
    mst_set = set()  # set of nodes included into MST
    rest_set = set(G.nodes())  # set of nodes not yet included into MST
    mst_edges = set()  # set of edges constituting MST
    

    mst_set.add(start_node)
    rest_set.remove(start_node)

    pq = PriorityQueue()

    new_node = '0'
    while rest_set: 
        # Adding new edges
        for node_neighbor in G.neighbors(new_node):
            if (not node_neighbor in mst_set):
                pq.put(
                        (
                            G.edges[new_node, node_neighbor]["weight"],
                            (new_node, node_neighbor)
                        )
                        )

        # Find min edge
        new_edge = pq.get()
        while new_edge[1][1] in mst_set:
            new_edge = pq.get()

        new_node = new_edge[1][1]
        mst_set.add(new_node)
        rest_set.remove(new_node)
        mst_edges.add(new_edge[1])

    return mst_edges


if __name__ == "__main__":
    G = nx.read_edgelist("practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    mst_edges = prim_mst(G, start_node="0")
    print(mst_edges)
    plot_graph(G, highlighted_edges=list(mst_edges))
