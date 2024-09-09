from collections import defaultdict, deque
 
def find_order(words):
    graph = defaultdict(set)
    in_degree = defaultdict(int)
 
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_length = min(len(word1), len(word2))
        for j in range(min_length):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break
        else:
            if len(word1) > len(word2):
                return "Invalid input. Longer word comes before its prefix."
 
    queue = deque([node for node in graph if in_degree[node] == 0])
    order = []
 
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
 
    if len(order) != len(graph):
        return "Invalid input. The input contains a cycle."
 
    all_chars = set(''.join(words).replace('#', ''))
    ordered_chars = set(order)
    for char in all_chars:
        if char not in ordered_chars:
            order.append(char)
 
    return ''.join(order)
 
# Input reading
input_lines = []
while True:
    line = input()
    if line == '#':
        break
    input_lines.append(line)
 
# Output
output = find_order(input_lines)
print(output)