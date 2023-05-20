import queue
from typing import Any

import networkx as nx

from src.plotting import plot_graph


def visit(node: Any):
    print(f"Wow, it is {node} right here!")

def dfs_iterative(G: nx.Graph, node: Any):
    visited = {n: False for n in G}

    q = queue.LifoQueue()

    q.put(node)

    while not q.empty():
        current_node = q.get()

        if visited[current_node]:
            continue

        visited[current_node] = True
        visit(current_node)

        for n in G.neighbors(current_node):
            q.put(n)

def topological_sort(G: nx.DiGraph, node: Any):
    visited = {n: False for n in G}

    q = queue.LifoQueue()

    while list(G.predecessors(node)):
        node = list(G.predecessors(node))[0]
        print(node)

    q.put(node)

    while not q.empty():
        current_node = q.get()

        predecessors = [n for n in G.predecessors(current_node) if not visited[n]]

        if predecessors:
            continue

        if visited[current_node]:
            continue

        visited[current_node] = True
        visit(current_node)

        for n in G.successors(current_node):
            q.put(n)

if __name__ == "__main__":
    # Load and plot the graph
    graph_filename = "practicum_2/homework/graph_2.edgelist"
    G = nx.read_edgelist(graph_filename, create_using=nx.Graph)
    plot_graph(G)

    print("Iterative DFS")
    print("-" * 32)
    dfs_iterative(G, node="2")
    print()

    G = nx.read_edgelist(
        graph_filename, create_using=nx.DiGraph
    )
    plot_graph(G)
    print("Topological sort")
    print("-" * 32)
    topological_sort(G, node="3")
