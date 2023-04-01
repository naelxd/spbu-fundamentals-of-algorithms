from typing import Any

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

    while rest_set:
        best_edge = {
            "edge": (None, None),
            "weight": np.inf
        }
        
        new_node = None
        for node in mst_set:
            for node_neighbor in G.neighbors(node):
                if (not node_neighbor in mst_set and 
                    G.edges[node, node_neighbor]["weight"] < best_edge["weight"]):
                    best_edge["edge"] = (node, node_neighbor)
                    best_edge["weight"] = G.edges[node, node_neighbor]["weight"]
                    new_node = node_neighbor

        mst_set.add(new_node)
        rest_set.remove(new_node)
        mst_edges.add(best_edge["edge"])

    return mst_edges


if __name__ == "__main__":
    G = nx.read_edgelist("practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    mst_edges = prim_mst(G, start_node="0")
    plot_graph(G, highlighted_edges=list(mst_edges))
