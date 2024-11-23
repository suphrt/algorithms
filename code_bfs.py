from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque()
    queue.append([start])
    
    if start == end:
        return [start]
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        for neighbor in graph[node]:
            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                
                if neighbor == end:
                    return new_path
                else:
                    queue.append(new_path)
    
    return None
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'Y'],
    'D': ['B', 'E'],
    'E': ['B', 'F', 'Y'],
    'F': ['C', 'E'],
    'Y': ['C', 'E', 'F']
}

print(bfs_shortest_path(graph, 'A', 'Y'))
print(bfs_shortest_path(graph, 'F', 'B'))


