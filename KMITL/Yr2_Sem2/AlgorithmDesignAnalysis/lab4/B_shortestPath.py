from collections import deque

def shortest_path(graph, start, end):
    queue = deque([(start, [start])])

    while queue:
        current_node, path = queue.popleft()

        for neighbor in graph.get(current_node, []):
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

    return None

def main():
    graph = {}
    # try:
    num_nodes = int(input())
    start, end = map(int, input().split())

    while True:
        edge = input()
        edgea, edgeb = edge.split()
        if edgea == "0" and edgeb == "0":
            break

        u, v = map(int, edge.split())
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
    # except EOFError:
    #     pass

    path = shortest_path(graph, start, end)
    if path:
        print(" ".join(map(str, path)))
    else:
        print("No path")

if __name__ == "__main__":
    main()
