from typing import Any

import networkx as nx
import numpy as np

from src.plotting import plot_graph


def dijkstra_sp(G: nx.Graph, source_node="0") -> dict[Any, list[Any]]:
    shortest_paths = {}  # key = destination node, value = list of intermediate nodes
    distances = {}
    nodes_to_visit = []

    for node in G.nodes():
        distances[node] = np.inf
        shortest_paths[node] = ["0"]
        nodes_to_visit.append(node)

    distances[source_node] = 0

    while nodes_to_visit:
        # Getting node to visit with minimal distance
        curr_node = nodes_to_visit[0]
        for node in nodes_to_visit:
            if distances[node] < distances[curr_node]:
                curr_node = node

        nodes_to_visit.remove(curr_node)

        for neighbor in G.neighbors(curr_node):
            dist = distances[curr_node] + G[curr_node][neighbor]["weight"]
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                shortest_paths[neighbor] = shortest_paths[curr_node] + [neighbor]

    return shortest_paths


if __name__ == "__main__":
    G = nx.read_edgelist("practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    shortest_paths = dijkstra_sp(G, source_node="0")
    test_node = "5"
    shortest_path_edges = [
        (shortest_paths[test_node][i], shortest_paths[test_node][i + 1])
        for i in range(len(shortest_paths[test_node]) - 1)
    ]
    plot_graph(G, highlighted_edges=shortest_path_edges)
