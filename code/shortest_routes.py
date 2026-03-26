from collections import deque
import networkx as nx


def bfs_shortest_path(graph, start_node):
    """
    Perform BFS to find the shortest path from the start node to every other node.
    Returns a dictionary with nodes as keys and their shortest distances as values.
    """
    visited = set()
    queue = deque([(start_node, 0)])  # Queue stores (node, distance)
    shortest_paths = {start_node: 0}  # Dictionary to store shortest paths

    while queue:
        current_node, current_distance = queue.popleft()

        # Process neighbors
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                shortest_paths[neighbor] = current_distance + 1
                queue.append((neighbor, current_distance + 1))

    return shortest_paths


def find_all_shortest_routes():
    G = create_combined_graph()
    start_node = "College Place"
    shortest_routes = bfs_shortest_path(G, start_node)

    print("\nShortest paths from College Place:")
    for target_node, distance in shortest_routes.items():
        print(f"Shortest route from {start_node} to {target_node}: {distance}")


def create_combined_graph():
    """Creates a combined graph from all loops."""
    G = nx.DiGraph()
    CP = "College Place"

    loops = {
        "SC": [(CP, "Comstock Lot"), ("Comstock Lot", "Colvin Lot"), ("Colvin Lot", "Small & Lambreth"),
               ("Small & Lambreth", "Slocum & Lambreth"), ("Slocum & Lambreth", "Winding Ridge"),
               ("Winding Ridge", "Skytop"), ("Skytop", "Goldstein")],
        "O": [(CP, "Flint"), ("Flint", "Shaw"), ("Shaw", "Barnes"), ("Barnes", "Forestry Gate"),
              ("Forestry Gate", "BBB"), ("BBB", "Campus West"), ("Campus West", "Henry St. Lot"),
              ("Henry St. Lot", "Lawrinson"), ("Lawrinson", "Irving Garage"), ("Irving Garage", "Quad Lot"),
              ("Quad Lot", "NVRC"), ("NVRC", "North Lot"), ("North Lot", "Schine"),
              ("Schine", "Comstock Ave"), ("Comstock Ave", "Dellplain")],
        "B": [(CP, "Comstock Ave"), ("Comstock Ave", "Waverly Ave"), ("Waverly Ave", "Walnut Ave"),
              ("Walnut Ave", "North"), ("North", "NVRC"), ("NVRC", "Quad Lot"),
              ("Quad Lot", "BBB"), ("BBB", "Campus West"), ("Campus West", "Henry St. Lot"),
              ("Henry St. Lot", "Irving Garage"), ("Irving Garage", "Sadler"), ("Sadler", "Barnes"),
              ("Barnes", "Sims Drive"), ("Sims Drive", "Flint"), ("Flint", "Shaw")],
        "WH": [(CP, "BBB"), ("BBB", "Syracuse Stage"), ("Syracuse Stage", "Peck Hall"),
               ("Peck Hall", "Warehouse")],
        "E": [(CP, "Genesee Irving"), ("Genesee Irving", "Genesee Crouse"),
              ("Genesee Crouse", "Genesee Westcott"), ("Genesee Westcott", "Westcott Euclid")]
    }

    for loop in loops.values():
        G.add_edges_from(loop)

    return G


if __name__ == "__main__":
    find_all_shortest_routes()
