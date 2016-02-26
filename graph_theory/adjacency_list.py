def bfsRecursive():
    return


def bfsIterative():
    return


def dfsRecursive(graph, source, blacklist=None):
    """
    Find all child vertices visited from
    source vertically & recursively.
    """
    if blacklist is None:
        blacklist = set()
    blacklist.add(source)
    for vertex in graph[source] - blacklist:
        dfsRecursive(graph, vertex, blacklist)
    return blacklist


def dfsIterative(graph, source):
    """
    Find all child vertices visited from
    source vertically & iteratively.
    """
    blacklist = set()
    stack = [source]
    while stack:
        vertex = stack.pop()
        if vertex not in blacklist:
            blacklist.add(vertex)
            stack.extend(graph[vertex] - blacklist)
    return blacklist


def createDirectedAdjacencyList(links):
    """ From a list of links between vertex,
    it returns a dict of neighboors """
    adjL = dict()

    for link in links:
        if not link[0] in adjL:
            adjL[link[0]] = set()
        if not link[1] in adjL:
            adjL[link[1]] = set()
        adjL[link[0]].add(link[1])

    return adjL

def createUndirectedAdjacencyList(links):
    """ From a list of links between vertex,
    it returns a dict of neighboors """
    adjL = dict()

    for link in links:
        if not link[0] in adjL:
            adjL[link[0]] = set()
        adjL[link[0]].add(link[1])
        if not link[1] in adjL:
            adjL[link[1]] = set()
        adjL[link[1]].add(link[0])

    return adjL



if __name__ == "__main__":
    l = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 5)]
    dRes = createDirectedAdjacencyList(l)
    UDRes = createUndirectedAdjacencyList(l)
    print dRes
    print UDRes

    print dfsIterative(dRes, 2)
    print dfsRecursive(dRes, 2)
    print dfsIterative(UDRes, 2)
    print dfsRecursive(UDRes, 2)

