import networkx as nx
import matplotlib.pyplot as plt
import scipy

def show_graph():
# Create a graph
    SC = nx.DiGraph()
    O = nx.DiGraph()
    B = nx.DiGraph()
    WH = nx.DiGraph()
    E = nx.DiGraph()

    CP = 'College Place' # position where all routes start !

    # South Campus Loop stops
    SC_stops = {1: CP, 2: "Comstock Lot", 3: "Colvin Lot", 4: "Small & Lambreth",
                5: "Slocum & Lambreth", 6: "Winding Ridge", 7: "Skytop", 8: "Goldstein"}

    # Orange Loop stops
    Orange_stops = {1: CP, 2: "Flint", 3: "Shaw", 4: "Barnes", 5: "Forestry Gate",
                    6: "BBB", 7: "Campus West", 8: "Henry St. Lot",
                    9: "Lawrinson", 10: "Irving Garage", 11: "Quad Lot", 12: "NVRC",
                    13: "North Lot", 14: "Schine", 15: "Comstock Ave", 16: "Dellplain"}

    # Blue Loop stops
    Blue_stops = {1: CP, 2: "Comstock Ave", 3: "Waverly Ave", 4: "Walnut Ave",
                  5: "North", 6: "NVRC", 7: "Quad Lot", 8: "BBB",
                  9: "Campus West", 10: "Henry St. Lot", 11: "Irving Garage",
                  12: "Sadler", 13: "Barnes", 14: "Sims Drive", 15: "Flint", 16: "Shaw" }

    # Warehouse Loop stops
    WH_stops = {1:CP, 2: "BBB", 3: "Syracuse Stage", 4: "Peck Hall", 5: "Warehouse"}

    # Euclid Loop stops
    Euc_stops = {1:CP, 2: "Genesee Irving", 3: "Genesee Crouse", 4: "Genesee Westcott",
                 5: "Westcott Euclid"}

# Create a list of edges and weights
    SC_Loop = [(SC_stops[1], SC_stops[2], 6), (SC_stops[2], SC_stops[3], 2), (SC_stops[3], SC_stops[4], 6), (SC_stops[4], SC_stops[5], 2),
               (SC_stops[5], SC_stops[6], 2), (SC_stops[6], SC_stops[7], 2), (SC_stops[7], SC_stops[8], 2), (SC_stops[8],
                SC_stops[1], 18)]

    Orange_Loop = [(Orange_stops[1], Orange_stops[2], 4), (Orange_stops[2], Orange_stops[3], 2), (Orange_stops[3], Orange_stops[4], 2),
                   (Orange_stops[4], Orange_stops[5], 3), (Orange_stops[5], Orange_stops[6], 2), (Orange_stops[6], Orange_stops[7], 1),
                   (Orange_stops[7], Orange_stops[8], 1), (Orange_stops[8], Orange_stops[9], 1), (Orange_stops[9], Orange_stops[10], 5),
                   (Orange_stops[10], Orange_stops[11], 5), (Orange_stops[11], Orange_stops[12], 3), (Orange_stops[12], Orange_stops[13], 2),
                   (Orange_stops[13], Orange_stops[14], 2), (Orange_stops[14], Orange_stops[15], 2), (Orange_stops[15], Orange_stops[16], 2),
                   (Orange_stops[16], Orange_stops[1], 2)]

    Blue_Loop =[(Blue_stops[1], Blue_stops[2], 3), (Blue_stops[2], Blue_stops[3], 2), (Blue_stops[3], Blue_stops[4], 2),
                (Blue_stops[4], Blue_stops[5], 1),(Blue_stops[5], Blue_stops[6], 2), (Blue_stops[6], Blue_stops[7], 2),
                (Blue_stops[7], Blue_stops[8], 4), (Blue_stops[8], Blue_stops[9], 1), (Blue_stops[9], Blue_stops[10], 1),
                (Blue_stops[10], Blue_stops[11], 5), (Blue_stops[11], Blue_stops[12], 1), (Blue_stops[12], Blue_stops[13], 3),
                (Blue_stops[13], Blue_stops[14], 1), (Blue_stops[14], Blue_stops[15], 5), (Blue_stops[15], Blue_stops[16], 5),
                (Blue_stops[16], Blue_stops[1], 2)]

    WH_Loop = [(WH_stops[1], WH_stops[2], 2), (WH_stops[2], WH_stops[3], 3), (WH_stops[3], WH_stops[4], 5),
                (WH_stops[4], WH_stops[5], 5),
               (WH_stops[5], WH_stops[1], 20)]

    Euc_Loop = [(Euc_stops[1], Euc_stops[2], 7), (Euc_stops[2], Euc_stops[3], 1), (Euc_stops[3], Euc_stops[4], 4),
                (Euc_stops[4], Euc_stops[5], 2),
                (Euc_stops[5], Euc_stops[1], 9)]

# Add all edges to the graph
    SC.add_weighted_edges_from(SC_Loop)
    O.add_weighted_edges_from(Orange_Loop)
    B.add_weighted_edges_from(Blue_Loop)
    WH.add_weighted_edges_from(WH_Loop)
    E.add_weighted_edges_from(Euc_Loop)

# Visualize the graph
    all_graphs = nx.compose_all([SC, O, B, WH, E])
    shared_layout = nx.spring_layout(all_graphs)

    nx.draw(SC, shared_layout, with_labels=True, edge_color='purple')
    nx.draw(O, shared_layout, with_labels=True, edge_color='orange')
    nx.draw(B, shared_layout, with_labels=True, edge_color='blue')
    nx.draw(WH, shared_layout, with_labels=True, edge_color='red')
    nx.draw(E, shared_layout, with_labels=True, edge_color='green')

# Draw edge labels with weights
    edge_labels1 = nx.get_edge_attributes(SC, 'weight')
    edge_labels2 = nx.get_edge_attributes(O, 'weight')
    edge_labels3 = nx.get_edge_attributes(B, 'weight')
    edge_labels4 = nx.get_edge_attributes(WH, 'weight')
    edge_labels5 = nx.get_edge_attributes(E, 'weight')

    nx.draw_networkx_edge_labels(SC, shared_layout, edge_labels=edge_labels1)
    nx.draw_networkx_edge_labels(O, shared_layout, edge_labels=edge_labels2)
    nx.draw_networkx_edge_labels(B, shared_layout, edge_labels=edge_labels3)
    nx.draw_networkx_edge_labels(WH, shared_layout, edge_labels=edge_labels4)
    nx.draw_networkx_edge_labels(E, shared_layout, edge_labels=edge_labels5)
    plt.show()

    print(list(nx.bfs_tree(all_graphs, CP)))
if __name__ == "__main__":
    show_graph()
