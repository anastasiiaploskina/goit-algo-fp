
import heapq

import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_edge("A", "B", weight=4)
G.add_edge("A", "C", weight=8)
G.add_edge("A", "E", weight=8)
G.add_edge("B", "C", weight=3)
G.add_edge("B", "F", weight=4)
G.add_edge("C", "D", weight=5)
G.add_edge("C", "F", weight=4)
G.add_edge("E", "C", weight=10)
G.add_edge("E", "F", weight=2)
G.add_edge("F", "G", weight=2)
G.add_edge("F", "H", weight=9)
G.add_edge("G", "D", weight=6)
G.add_edge("G", "H", weight=1)
G.add_edge("H", "D", weight=3)


def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > shortest_paths[current_vertex]:
            continue
        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes.get("weight", 1)
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return shortest_paths


shortest_paths = dijkstra(G, "A")
print(shortest_paths)

pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()
