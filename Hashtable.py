from Hash import DSAHashTable
from Hash import DSAHashEntry

class HashTable:
    def __init__(self):
        self.capacity = 100
        self.size = 0
        self.buckets = [None] * self.capacity
    
    def hash(self, key):
        """Calculates the hash value of a key."""
        hash_sum = 0
        for i, c in enumerate(key):
            hash_sum += (i + len(key)) ** ord(c)
            hash_sum = hash_sum % self.capacity
        return hash_sum
    
    def insert(self, key, value):
        """Inserts a key-value pair into the hash table."""
        index = self.hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = []
        for pair in self.buckets[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[index].append([key, value])
        self.size += 1
        
    def get(self, key):
        """Retrieves the value associated with a key from the hash table."""
        index = self.hash(key)
        if self.buckets[index] is None:
            return None
        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]
        return None
        
    def remove(self, key):
        """Removes a key-value pair from the hash table."""
        index = self.hash(key)
        if self.buckets[index] is None:
            return None
        for i, pair in enumerate(self.buckets[index]):
            if pair[0] == key:
                self.size -= 1
                return self.buckets[index].pop(i)
        return None


def read_graph(filename):      #read graph file
    """Reads the graph data from a file and stores it in a hash table."""
    graph = HashTable()
    with open(filename) as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                start, end, weight = parts
                graph.insert((start, end), float(weight))
    return graph


def read_data(filename):    #read data file
    """Reads the UAV data from a file and stores it in a hash table."""
    data = HashTable()
    with open(filename) as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 4:
                location, x, y, z = parts
                data.insert(location, (int(x), int(y), int(z)))
    return data


if __name__ == '__main__':
    # Get the file names from the user
    graph_file = input('Input the name of the graph file: ')
    data_file = input('Input the name of the data file: ')
    
    # Read the graph and data into hash tables
    graph = read_graph(graph_file)
    data = read_data(data_file)
    
    # Get a location from the user and print its data
    location = input('Enter a location: ')
    location_data = data.get(location)
    if location_data is None:
        print('No data found for location:', location)
    else:
        print('Data of location {}:'.format(location))
        print('temperature:', location_data[0])
        print('humidity:', location_data[1])
        print('wind speed:', location_data[2])
