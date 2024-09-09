from collections import defaultdict
 
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0
 
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    def articulation_points_util(self, u, visited, ap, parent, low, disc):
        children = 0
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
 
        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                self.articulation_points_util(v, visited, ap, parent, low, disc)
 
                low[u] = min(low[u], low[v])
 
                if parent[u] == -1 and children > 1:
                    ap[u] = True
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
 
    def articulation_points(self):
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)
        ap = [False] * (self.V)
 
        for i in range(self.V):
            if not visited[i]:
                self.articulation_points_util(i, visited, ap, parent, low, disc)
 
        result = [i for i, x in enumerate(ap) if x]
        return sorted([x + 1 for x in result])  # Adjusting 0-based index to 1-based
 
n = int(input())
g = Graph(n)
while True:
    u, v = map(int, input().split())
    if u == 0 and v == 0:
        break
    g.add_edge(u-1, v-1)
 
print(*g.articulation_points())