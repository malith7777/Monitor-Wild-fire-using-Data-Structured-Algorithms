from collections import defaultdict
import heapq

class DSAGraph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, start, end, weight):
        self.adjacency_list[start].append((end, weight))
        self.adjacency_list[end].append((start, weight))

def read_graph(file_name):
    graph = DSAGraph()
    nodes = set()

    with open(file_name, 'r') as file:
        lines = file.readlines()
        num_nodes, num_edges = map(int, lines[0].split())

        for line in lines[1:]:
            start, end, weight = line.split()
            graph.add_edge(start, end, float(weight))
            nodes.add(start)
            nodes.add(end)

    return graph, nodes

def dijkstra(graph, nodes, start):  #used w3school
    distances = {node: float('inf') for node in nodes}
    distances[start] = 0

    heap = [(0, start)]
    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_dist > distances[current_node]:
            continue

        for neighbor, edge_weight in graph.adjacency_list[current_node]:
            new_distance = current_dist + edge_weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return distances

#  user to input the file names
graph_file = input("Input the file name for the graph data: ")
data_file = input("Input the file name for the UAV data: ")

# Read data from the graph file 
graph, graph_nodes = read_graph(graph_file)

# Read data from the UAV data file 
heap = []
with open(data_file, "r") as file:
    for line in file:
        area, temp, hum, wind = line.split()

        # Calculate the risk level
        temp_risk = 3 if int(temp) > 40 else (2 if int(temp) > 32 else 1)
        hum_risk = 1 if int(hum) < 30 else (2 if int(hum) < 50 else 3)
        wind_risk = 1 if int(wind) < 40 else (2 if int(wind) < 55 else 3)
        risk_level = temp_risk + hum_risk + wind_risk

        
        heapq.heappush(heap, (-risk_level, area))

# Output the highest risk value areas
print("Highest risk value areas:")
for i in range(1):
    if heap:
        risk_count, area = heapq.heappop(heap)
        print(area)

#  user to input the number of UAVs
while True:
    try:
        num_uavs = int(input("Input the number of UAVs: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number of UAVs.")

# user to input the starting positions of UAVs
starting_positions = []
for i in range(num_uavs):
    position = input(f"Input the starting position for UAV {i+1}: ")
    starting_positions.append(position)

# generate flight paths for each UAV
flight_paths = []
for i in range(num_uavs):
    uav_path = dijkstra(graph, graph_nodes, starting_positions[i])
    flight_paths.append(uav_path)

for i, path in enumerate(flight_paths):
    uav_id = f"UAV_{i+1}"
    print(f"\n{uav_id}:")
    path_list = list(path.keys())
    path_list.remove(starting_positions[i])
    path_list.append(starting_positions[i])
    print(" <- ".join(path_list), end=" <- ")
print()

