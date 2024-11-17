def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def connected_components(graph):
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            component = set()
            dfs(graph, node, component)
            components.append(component)
            visited.update(component)
    return components

graph = {
'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A', 'F'],
'D': ['B'],
'E': ['B', 'F'],
'F': ['C', 'E'],
'G': ['H'],
'H': ['G']
}
graph1 = {}

print("Поиск в глубину от вершины H:")
print(dfs(graph, 'H'))

print("Поиск в глубину от вершины C:")
print(dfs(graph, 'C'))

print("\nКомпоненты связности:" )
print(connected_components(graph))

print("\nКомпоненты связности в пустом графе:" )
print(connected_components(graph1))
