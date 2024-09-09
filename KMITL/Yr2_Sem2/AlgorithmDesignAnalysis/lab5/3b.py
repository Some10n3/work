from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = defaultdict(list)
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def DFSUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited, stack)
        stack = stack.append(v)
 
    def transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g
 
    def fillOrder(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.fillOrder(i, visited, stack)
        stack.append(v)
 
    def getSCCs(self):
        stack = []
        visited = [False] * (self.V + 1)
        for i in range(1, self.V + 1):
            if not visited[i]:
                self.fillOrder(i, visited, stack)
 
        gr = self.transpose()
         
        visited = [False] * (self.V + 1)
 
        sccs = []
        while stack:
            i = stack.pop()
            if not visited[i]:
                scc = []
                gr.DFSUtil(i, visited, scc)
                sccs.append(sorted(scc))
        return sorted(sccs, key=lambda x: x[0])
 
def process_input(input_data):
    # Split the input data into lines
    lines = input_data.strip().split('\n')
    # Get the number of vertices
    vertices = int(lines[0])
    # Initialize the graph
    g = Graph(vertices)
 
    # Process each edge
    for i in range(1, len(lines)):
        u, v = map(int, lines[i].split())
        if u == 0 and v == 0:  # End of input
            break
        g.addEdge(u, v)
 
    # Get SCCs and format the output
    sccs = g.getSCCs()
    output = '\n'.join(' '.join(map(str, scc)) for scc in sccs)
    return output
 
n = int(input())
edges = []
while True:
    u, v = map(int, input().split())
    if u == 0 and v == 0:
        break
    edges.append((u, v))
 
# process input
input_data = f"{n}\n" + '\n'.join(f"{u} {v}" for u, v in edges)
print(process_input(input_data))