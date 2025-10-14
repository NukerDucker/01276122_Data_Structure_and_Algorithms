def build_graph(input_string):
    graph = {}
    start_node = None
    edges = [e.strip() for e in input_string.split(',')]

    for edge_str in edges:
        source, dest = edge_str.split()
        graph.setdefault(source, []).append(dest)
        graph.setdefault(dest, []).append(source)
        if start_node is None:
            start_node = source

    return graph, start_node


def dfs_traversal(graph, start_node, visited):
    if start_node is None:
        return []

    stack = [start_node]
    traversal_order = []
    visited.add(start_node)

    while stack:
        current_node = stack.pop()
        traversal_order.append(current_node)
        neighbors = sorted(graph.get(current_node, []), reverse=True)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return traversal_order


def bfs_traversal(graph, start_node, visited):
    if start_node is None:
        return []

    queue = [start_node]
    traversal_order = []
    visited.add(start_node)

    while queue:
        current_node = queue.pop(0)
        traversal_order.append(current_node)
        neighbors = sorted(graph.get(current_node, []))

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


def traverse_graph(graph, traversal_function):
    visited = set()
    result = []
    for node in sorted(graph.keys()):
        if node not in visited:
            component_result = traversal_function(graph, node, visited)
            result.extend(component_result)

    return result


def main():
    print(" *** Graph Traversal ***")
    input_str = input('Enter : ')

    graph, _ = build_graph(input_str)

    dfs_result = traverse_graph(graph, dfs_traversal)
    bfs_result = traverse_graph(graph, bfs_traversal)

    print("Depth First Traversals :", *dfs_result)
    print("Bredth First Traversals :", *bfs_result)
    print("===== End of program =====")


if __name__ == "__main__":
    main()