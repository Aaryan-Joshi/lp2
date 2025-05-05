import heapq

def diijkstra(graph,start):
    dist = {node : float('inf') for node in graph }
    dist[start] = 0
    pq = [(0,start)]

    while pq:
        current_dist , current_node = heapq.heappop(pq)
        if current_dist > dist[current_node]:
            continue

        for neighbour,weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbour]:
                dist[neighbour] = distance
                heapq.heappush(pq,(distance,neighbour))

    return dist

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

print(diijkstra(graph,'A')) 