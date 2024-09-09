from collections import defaultdict

def dfs(graph, node, visited, disc, low, parent, ap):
    children = 0
    visited[node] = True
    disc[node] = low[node] = len(visited)
    for child in graph[node]:
        if not visited[child]:
            children += 1
            parent[child] = node
            dfs(graph, child, visited, disc, low, parent, ap)
            low[node] = min(low[node], low[child])
            if parent[node] == -1 and children > 1:
                ap[node] = True
            if parent[node] != -1 and low[child] >= disc[node]:
                ap[node] = True
        elif child != parent[node]:
            low[node] = min(low[node], disc[child])

def find_articulation_points(graph, n):
    visited = [False] * (n + 1)
    disc = [0] * (n + 1)
    low = [0] * (n + 1)
    parent = [-1] * (n + 1)
    ap = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited, disc, low, parent, ap)
    return [i for i in range(1, n + 1) if ap[i]]

def main():
    n = int(input())
    graph = defaultdict(list)
    while True:
        a, b = map(int, input().split())
        if a == b == 0:
            break
        graph[a].append(b)
        graph[b].append(a)
    ap = find_articulation_points(graph, n)
    print(' '.join(map(str, ap)))

if __name__ == "__main__":
    main()