import networkx as nx
import matplotlib.pyplot as plt
import scipy

def show_graph():
# Create a graph
    G = nx.DiGraph()
    F = nx.DiGraph()

# Create a list of edges and weights
    weighted_edges1 = [('S', 1, 10), ('S', 2, 15), (1, 3, 5), (1, 2, 6),
    (2, 4, 10), (4, 3, 5), (3, 'T', 7), (4, 'T', 8)]
    weighted_edges2 = [('S', 3, 10), ('S', 'T', 20), (2, 'T', 10)]

# Add all edges to the graph
    G.add_weighted_edges_from(weighted_edges1)
    F.add_weighted_edges_from(weighted_edges2)

# Visualize the graph
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, with_labels=True, edge_color='skyBlue')
    nx.draw(F, pos, with_labels=True, edge_color='red')

# Draw edge labels with weights
    edge_labels1 = nx.get_edge_attributes(G, 'weight')
    edge_labels2 = nx.get_edge_attributes(F, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels1)
    nx.draw_networkx_edge_labels(F, pos, edge_labels=edge_labels2)
    plt.show()

if __name__ == "__main__":
    show_graph()