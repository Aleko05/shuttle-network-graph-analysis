import networkx as nx
import matplotlib.pyplot as plt
import scipy

def bfs_tree(G, source, reverse=False, depth_limit=None, sort_neighbors=None):
    T = nx.DiGraph()
    T.add_node(source)
    edges_gen = bfs_edges(
        G,
        source,
        reverse=reverse,
        depth_limit=depth_limit,
        sort_neighbors=sort_neighbors,
    )
    T.add_edges_from(edges_gen)
    return T

    return show.graph(T)
