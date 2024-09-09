def bfs (graph, node):
    visited = []
    queue = []
    result = []

    visited.append(node)
    queue.append(node)

    while queue:
        print(queue)
        m = queue.pop(0)
        # print (m, end = " ")
        result.append(m)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return result

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

print (bfs(graph, 'A'))