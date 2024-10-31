from DSALinkedList import DSALinkedList
from DSALinkedList import DSALinkedListIterator
from DSAQueue import DSAQueue
from DSAStack import DSAStack

def read_graph(file_name):    #read graph file
    """Reads graph from file."""
    graph = {}
    with open(file_name) as f:
        x, y = map(int, f.readline().strip().split())
        for i in range(y):
            a, b, c = f.readline().strip().split()
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = float(c)
            graph[b][a] = float(c)
    return graph

def read_data(file_name):      #read data file
    """Reads UAV data from file."""
    data = {}
    with open(file_name) as f:
        for line in f:
            node, temp, hum, wind = line.strip().split()
            data[node] = {'temperature': int(temp), 'humidity': int(hum), 'wind speed': int(wind)}
    return data

def breadth_first_search(graph, data, start, end):
    """Finds the shortest path between two locations using BFS."""
    queue = DSAQueue()
    visited = set()
    queue.enqueue((start, []))
    while not queue.is_empty():
        node, path = queue.dequeue()
        if node == end:
            return path + [node]
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            queue.enqueue((neighbor, path + [node]))
    return None

def depth_first_search(graph, data, node, visited):
    """Explores the entire graph using DFS."""
    if node in visited:
        return
    visited.add(node)
    print(f'{node}: temperature={data[node]["temperature"]}C, humidity={data[node]["humidity"]}, wind speed={data[node]["wind speed"]}km/h')
    for neighbor in graph[node]:
        depth_first_search(graph, data, neighbor, visited)

if __name__ == '__main__':
    try:
        graph_file = input("Enter the graph file name: ")
        data_file = input("Enter the data file name: ")
        graph = read_graph(graph_file)
        data = read_data(data_file)
    except Exception as e:
        print(f'Error reading input files: {e}')
        exit(1)

    start = input('Input the starting location: ').strip().upper()
    end = input('Input the ending location: ').strip().upper()

    if start not in graph or end not in graph:
        print('Invalid location')
        exit(1)

    shortest_path = breadth_first_search(graph, data, start, end)
    if shortest_path is None:
        print('No path found')
    else:
        print(f'Shortest path of {start} and {end}:', shortest_path)
        for node in shortest_path:
            print(f'{node}: temperature={data[node]["temperature"]}C, humidity={data[node]["humidity"]}, wind speed={data[node]["wind speed"]}km/h')

    print('UAV data for the graph:')
    visited = set()
    depth_first_search(graph, data, start, visited)

