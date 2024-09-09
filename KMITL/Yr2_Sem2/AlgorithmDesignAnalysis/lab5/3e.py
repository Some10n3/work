import math
 
def get_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
 
def min_cost_to_connect_cities(cities):
    n = len(cities)
    adj_matrix = [[0] * n for _ in range(n)]
 
    # Building the adjacency matrix with distances
    for i in range(n):
        for j in range(i + 1, n):
            distance = get_distance(cities[i], cities[j])
            adj_matrix[i][j] = adj_matrix[j][i] = distance
 
    # Applying Prim's algorithm to find the Minimum Spanning Tree (MST)
    selected = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0
    parent = [-1] * n
    total_cost = 0
 
    for _ in range(n):
        # Find the vertex with the minimum edge weight
        u = min((v for v in range(n) if not selected[v]), key=lambda v: min_edge[v])
 
        # Add the vertex to the MST
        selected[u] = True
        total_cost += min_edge[u]
 
        # Update the edge weights
        for v in range(n):
            if adj_matrix[u][v] > 0 and not selected[v] and adj_matrix[u][v] < min_edge[v]:
                min_edge[v] = adj_matrix[u][v]
                parent[v] = u
 
    return total_cost
 
# Input handling
n = int(input())
cities = []
for _ in range(n):
    x, y = map(float, input().split())
    cities.append((x, y))
 
# Calculating the minimum cost
min_cost = min_cost_to_connect_cities(cities)
#print with at most 2 decimal places
print(f'{min_cost:.1f}' if min_cost.is_integer() else f'{min_cost:.2f}')
