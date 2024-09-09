from collections import deque

class DGraphAdjLst():
  def __init__(self, N):
    self.adjLst = [deque() for j in range(N)]
    self.numNodes = N
    self.numEdges = 0

  def addEdge(self,u,v):
    if not self.isAdjacent(u,v):
      self.adjLst[u].append(v)
      self.numEdges+=1

  def removeEdge(self,u,v):
    if self.isAdjacent(u,v):
      self.adjLst[u].remove(v)
      self.numEdges-=1

  def isAdjacent(self,u,v):
    for w in self.adjLst[u]:
      if w == v:
        return True
    return False

  def neighbors(self,u):
    return list(self.adjLst[u])

  def edges(self):
    L = []
    for u in range(self.numNodes):
      for v in self.adjLst[u]:
          L.append((u,v))
    return L

def findVisitable(G, u):
    visitable = [False]*G.numNodes
    queue = deque()
    queue.append(u)

    for v in G.neighbors(u):
        queue.append(v)
        visitable[v] = True
    while queue:
        u = queue.popleft()
        for v in G.neighbors(u):
            if not visitable[v]:
                queue.append(v)
                visitable[v] = True

    for i in range(G.numNodes):
        if visitable[i]:
            print(i+1, end=" ")
  

number = int(input())
G1 = DGraphAdjLst(number)
start = int(input())

while True:
    a = input().split()
    u = int(a[0])
    v = int(a[1])
    if u == 0 and v == 0:
        break
    G1.addEdge(u-1, v-1)

findVisitable(G1, start-1)