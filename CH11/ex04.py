def create_adj_list(edges):
    max_node = -1
    for edge in edges:
        src, dest = [int(e) for e in edge.split()]
        if src > max_node:
            max_node = src
        if dest > max_node:
            max_node = dest
    size = max_node + 1

    adj_list = []
    for _ in range(size):
        adj_list.append([])

    return adj_list


def has_cycle_dfs(edges, adj_list, visited, node=0):
    if node in visited:
        return True
    visited.append(node)

    for neighbor in adj_list[node]:
        if has_cycle_dfs(edges, adj_list, visited, neighbor):
            return True
    return False


def main():
    edges = input("Enter : ").split(',')
    adj_list = create_adj_list(edges)

    for edge in edges:
        src, dest = [int(e) for e in edge.split()]
        adj_list[src].append(dest)


    has_cycle = has_cycle_dfs(edges, adj_list, [])

    if has_cycle:
        print("Graph has a cycle")
    else:
        print("Graph has no cycle")

if __name__ == "__main__":
    main()