


def createIncidenceList(links):
    graph = dict()
    for i, link in enumerate(links):
        if link[0] not in graph:
            graph[link[0]] = set()
        graph[link[0]].add(i)
        if link[1] not in graph:
            graph[link[1]] = set()
        graph[link[1]].add(i)
    return graph




if __name__ == "__main__":
    l = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 5)]
    print createIncidenceList(l)
