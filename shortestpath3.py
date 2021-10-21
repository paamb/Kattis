import math

def bellman_ford(start, num_nodes, edges, adjacency_list):
    cost_to_node = [math.inf for i in range(num_nodes)]
    cost_to_node[start] = 0
    for i in range(num_nodes-1):
        shorter_path_in_it = False
        for edge in edges:
            from_node, to_node, weight = edge
            if cost_to_node[from_node] + weight < cost_to_node[to_node]:
                shorter_path_in_it = True
                if i == num_nodes-2 and num_nodes > 1 and len(edges) > 1:
                    bfs(to_node, cost_to_node, adjacentcy_list)
                    cost_to_node[to_node] = -math.inf

                else:
                    cost_to_node[to_node] = cost_to_node[from_node] + weight
        if not shorter_path_in_it:
            break
    return cost_to_node
def bfs(source, cost_to_node, adjacentcy_list):
    queue = [source]
    while queue:
        source = queue[0]
        queue.pop()
        for neighbour in adjacentcy_list[source]:
            if cost_to_node[neighbour] == -math.inf:
                continue    
            cost_to_node[neighbour] = -math.inf
            queue.append(neighbour)

            
while True:
    num_nodes, num_edges, queries, start = [int(x) for x in input().split()]
    adjacentcy_list = [[] for i in range(num_nodes)]
    edges = []

    if num_nodes == num_edges == queries == start == 0:
        break

    for i in range(num_edges):
        from_node, to_node, weight = [int(x) for x in input().split()]
        adjacentcy_list[from_node].append(to_node)
        edges.append((from_node, to_node, weight))

    cost_to_node = bellman_ford(start, num_nodes, edges, adjacentcy_list)

    for i in range(queries):
        end_node = int(input())
        if cost_to_node[end_node] == math.inf:
            print("Impossible")
        elif cost_to_node[end_node] == -math.inf:
            print("-Infinity")
        else:
            print(cost_to_node[end_node])