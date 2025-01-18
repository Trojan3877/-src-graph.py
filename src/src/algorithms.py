import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.get_neighbors(current_node):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def pagerank(graph, alpha=0.85, iterations=100):
    nodes = graph.graph.keys()
    rank = {node: 1 / len(nodes) for node in nodes}

    for _ in range(iterations):
        new_rank = {}
        for node in nodes:
            rank_sum = sum(rank[neighbor] for neighbor, _ in graph.get_neighbors(node))
            new_rank[node] = (1 - alpha) / len(nodes) + alpha * rank_sum
        rank = new_rank

    return rank
