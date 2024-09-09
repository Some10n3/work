from collections import deque

# Declaring constants
UNDISCOVERED = 0
DISCOVERED = 1

def bfs(G,s):
  state = [UNDISCOVERED for i in range(G.numNodes)]
  Q = deque()
  state[s] = DISCOVERED
  Q.append(s)
  while len(Q)>0:
    u = Q.popleft()
    print("Exploring Node " + str(u))
    for v in G.neighbors(u):
      if state[v] == UNDISCOVERED:
        state[v] = DISCOVERED
        Q.append(v)




# Declaring constants
UNDISCOVERED = 0
DISCOVERED = 1

def dfs(G,s):
  state = [UNDISCOVERED for i in range(G.numNodes)]
  S = []
  state[s] = DISCOVERED
  S.append(s)
  while len(S)>0:
    u = S.pop()
    print("Exploring Node " + str(u))
    for v in G.neighbors(u):
      if state[v] == UNDISCOVERED:
        state[v] = DISCOVERED
        S.append(v)