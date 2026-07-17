import heapq


def dijkstra(graph, source):
    """
    Dijkstra's Algorithm using Min-Heap
    Time Complexity: O((V + E) log V)
    Space Complexity: O(V)

    graph: Dictionary {vertex: [(neighbor, weight), ...]}
    source: Source vertex
    """
    n = len(graph)

    # Initialize distances and previous vertices
    dist = [float('inf')] * n
    prev = [None] * n
    dist[source] = 0

    # Priority Queue: (distance, vertex)
    pq = [(0, source)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        # Relax all adjacent edges
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, prev


def reconstruct_path(prev, source, target):
    """
    Reconstructs the shortest path from source to target.
    """
    path = []
    node = target

    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()

    if path and path[0] == source:
        return path
    return []


# ---------------- Graph Definition ----------------

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: [(5, 2)],
    5: []
}

source = 0

# Run Dijkstra's Algorithm
dist, prev = dijkstra(graph, source)

# Display Results
print(f"Shortest paths from vertex {source}:\n")

print("{:>8} {:>10} {:>30}".format("Vertex", "Distance", "Path"))
print("-" * 55)

for v in range(len(graph)):
    path = reconstruct_path(prev, source, v)
    path_str = " -> ".join(map(str, path)) if path else "No path"
    distance = dist[v] if dist[v] != float('inf') else "INF"

    print("{:>8} {:>10} {:>30}".format(v, str(distance), path_str))