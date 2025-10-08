def sort_key(x):
    if x.isalpha():
        return (1, x.lower())
    return (0, int(x))

def main():
    print(' *** Directed Graph Adjacency Matrix ***')
    input_str = input('Enter : ')

    edges = [edge.split() for edge in input_str.split(',')]
    vertices = sorted({v for edge in edges for v in edge}, key=sort_key)
    
    n = len(vertices)
    matrix = [[0] * n for _ in range(n)]

    vertex_index = {v: i for i, v in enumerate(vertices)}

    for from_v, to_v in edges:
        i, j = vertex_index[from_v], vertex_index[to_v]
        matrix[i][j] = 1

    print("   ", "  ".join(vertices))
    for i, vertex in enumerate(vertices):
        row = ", ".join(map(str, matrix[i]))
        print(f"{vertex} : {row}")

    print("===== End of program ======")

if __name__ == "__main__":
    main()