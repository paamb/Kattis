import math
import heapq
import time
def bfs(start, num_nodes, adjacent_dic):
  value_of_nodes = [math.inf for i in range(num_nodes)]
  value_of_nodes[start] = 0
  queue = [(0,start)]
  heapq.heapify(queue)
  while queue:
    lowestPath = heapq.heappop(queue)
    cost, from_node = lowestPath
    if from_node not in adjacent_dic:
      continue
    for element in adjacent_dic[from_node]: 
      to_node, start_time, intervall, weight = element
      if cost <= start_time:
        cost_for_neighbour = cost + (start_time-cost) + weight
      elif cost > start_time:
        if intervall != 0:
          cost_for_neighbour = cost + (start_time-cost)%intervall + weight
        else:
          continue

      if cost_for_neighbour < value_of_nodes[to_node]:
        value_of_nodes[to_node] = cost_for_neighbour
        heapq.heappush(queue,(cost_for_neighbour, to_node))
  return value_of_nodes

while True:
  num_nodes, num_edges, queries, start = [int(x) for x in input().split()]
  start_time = time.time()
  adjacent_dic = {}

  if num_nodes == num_edges == queries == start == 0:
    break

  for i in range(num_edges):
    from_node, to_node, start_time, intervall, weight = [int(x) for x in input().split()]
    adjacent_dic.setdefault(from_node, []).append((to_node, start_time, intervall, weight))

  value_of_nodes = bfs(start, num_nodes, adjacent_dic)
  for i in range(queries):
    end_node = int(input())
    if value_of_nodes[end_node] == math.inf:
      print("Impossible")
    else:
      print(value_of_nodes[end_node])