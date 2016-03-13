

def dijkstra(matrix, vertices, start, end):
    # Initialze a distance to start's array to infinite
    distances = [float('inf')] * len(vertices)
    choice = start
    # Set the distance of start to itself to 0
    distances[choice] = 0
    visited, path = [], []

    while choice != end:
        dist_choice = min(distances)
        choice = distances.index(dist_choice)
        neighbors = [(d, v) for v, d in enumerate(matrix[choice]) if d != 0]
        for d, v in neighbors:
            if v not in visited:
                distplus = d + distances[choice]
                if distplus < distances[v]:
                    distances[v] = distplus
                    path.append([v, choice, distplus])
        visited.append(choice)
        distances[choice] = float('inf')
    x = choice
    result_str = "(" + str(x) + ")"
    while x != start:
        L = [l for l in path if l[0] == x]
        x = min(L, key = lambda x:x[2])[1]
        d = min(L, key = lambda x:x[2])[2]

        result_str = "(" + str(x) + ")-" + str(d) + "->" + result_str

    return result_str



def createAdjacencyMatrix(links, directed=False):
    vertices = set()

    for v1, v2, x in links:
        vertices.add(v1)
        vertices.add(v2)
    
    M = [[0 for x in range(len(vertices))]for x in range(len(vertices))]
    
    for v1, v2, weight in links:
        M[v1][v2] = weight
        if not directed:
            M[v2][v1] = weight

    return M, vertices



if __name__ == "__main__":
    l = [
         (0, 1, 3), (0, 2, 1), (1, 2, 1), (1, 3, 4), (1, 4, 1),
         (2, 3, 6), (2, 4, 5), (3, 4, 1), (3, 5, 1), (4, 5, 5)
        ]

    matrix, vertices = createAdjacencyMatrix(l, False)
    for line in matrix:
        print line
    
    print "= Dijkstra =============="
    print dijkstra(matrix, vertices, 1, 5)
