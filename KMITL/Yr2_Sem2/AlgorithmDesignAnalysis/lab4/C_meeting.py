def dfs_helper(node, c, adj_list, color):
    color[node] = c
    for neighbor in adj_list[node]:
        if color[neighbor] == c:
            return False
        if color[neighbor] == 0 and not dfs_helper(neighbor, -c, adj_list, color):
            return False
    return True

def create_groups(N, dislikes):
    adj_list = [[] for _ in range(N + 1)]
    for u, v in dislikes:
        adj_list[u].append(v)
        adj_list[v].append(u)

    color = [0] * (N + 1)

    for i in range(1, N + 1):
        if color[i] == 0 and not dfs_helper(i, 1, adj_list, color):
            return "Not possible"

    group1 = [i for i in range(1, N + 1) if color[i] == 1]
    group2 = [i for i in range(1, N + 1) if color[i] == -1]

    if not group1 or not group2:
        return "Not possible"

    return group1, group2

if __name__ == "__main__":
    # Input reading
    n = int(input())
    participant_preferences = []
    while True:
        u, v = map(int, input().split())
        if u == 0 and v == 0:
            break
        participant_preferences.append((u, v))

    # Output result
    result = create_groups(n, participant_preferences)
    if result == "Not possible":
        print(result)
    else:
        group_1, group_2 = result
        print(" ".join(map(str, group_1)))
        print(" ".join(map(str, group_2)))
