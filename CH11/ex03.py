def build_weighted_graph(edges_string):
    graph = {}
    edges = [e.strip() for e in edges_string.split(',')]

    for edge_str in edges:
        parts = edge_str.split()
        if len(parts) == 3:
            source, weight, dest = parts
            weight = int(weight)

            if source not in graph:
                graph[source] = []
            graph[source].append((dest, weight))

            if dest not in graph:
                graph[dest] = []

    return graph


def dijkstra(graph, start):
    distances = {node: 999999 for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}

    unvisited = set(graph.keys())

    while unvisited:
        current_node = None
        min_distance = 999999

        for node in unvisited:
            if distances[node] < min_distance:
                min_distance = distances[node]
                current_node = node

        if current_node is None or min_distance == 999999:
            break

        unvisited.remove(current_node)

        for neighbor, weight in graph.get(current_node, []):
            distance = distances[current_node] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node

    return distances, previous


def reconstruct_path(previous, start, end):
    if previous[end] is None and start != end:
        return None

    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path


def process_queries(graph, queries_string):
    queries = [q.strip() for q in queries_string.split(',')]
    results = []

    for query in queries:
        parts = query.split()
        if len(parts) == 2:
            start, end = parts

            if start not in graph:
                results.append(f"Not have path : {start} to {end}")
                continue
            if end not in graph:
                results.append(f"Not have path : {start} to {end}")
                continue

            distances, previous = dijkstra(graph, start)
            path = reconstruct_path(previous, start, end)

            if path is None or distances[end] == 999999:
                results.append(f"Not have path : {start} to {end}")
            else:
                path_str = "->".join(path)
                results.append(f"{start} to {end} : {path_str}")

    return results


def main():
    print(" *** Shortest Path (Dijkstra's Algorithm) ***")
    input_str = input('Enter : ')

    parts = input_str.split('/')
    if len(parts) != 2:
        print("Invalid input format")
        return

    edges_string = parts[0].strip()
    queries_string = parts[1].strip()

    graph = build_weighted_graph(edges_string)

    results = process_queries(graph, queries_string)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
