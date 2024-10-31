from Graph import DSAGraph
from Graph import DSAGraphNode
from DSALinkedList import DSALinkedList
from DSALinkedList import DSALinkedListIterator
from DSAQueue import DSAQueue

def display_graph(graph):
    print("Adjacency List:")
    for node in graph:
        neighbors = ", ".join(graph[node])
        print(f"{node}: {neighbors}")

def insert_edge(graph, label1, label2):
    if label1 not in graph:
        graph[label1] = set()

    if label2 not in graph:
        graph[label2] = set()

    graph[label1].add(label2)
    graph[label2].add(label1)
    print(f"Edge ({label1}, {label2}) inserted.")

def delete_edge(graph, label1, label2):
    if label1 in graph and label2 in graph[label1]:
        graph[label1].remove(label2)
        graph[label2].remove(label1)
        print(f"Edge ({label1}, {label2}) deleted.")
    else:
        print(f"Edge ({label1}, {label2}) not found.")

def search_edge(graph, label1, label2):
    if label1 in graph and label2 in graph[label1]:
        print(f"Edge ({label1}, {label2}) found.")
    else:
        print(f"Edge ({label1}, {label2}) not found.")

# Read graph data from a file
filename = input("Input filename: ")

try:
    with open(filename, "r") as f:
        graph = {}

        for line in f:
            tokens = line.split()
            label1 = tokens[0]
            label2 = tokens[1]
            insert_edge(graph, label1, label2)

        # Display initial graph
        display_graph(graph)

        # Interactive menu
        while True:
            print("\nMenu:")
            print("1. Insert ")
            print("2. Delete ")
            print("3. Search ")
            print("4. Display Graph")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                label1 = input("Enter the first node label: ")
                label2 = input("Enter the second node label: ")
                insert_edge(graph, label1, label2)
            elif choice == "2":
                label1 = input("Enter the first node label: ")
                label2 = input("Enter the second node label: ")
                delete_edge(graph, label1, label2)
            elif choice == "3":
                label1 = input("Enter the first node label: ")
                label2 = input("Enter the second node label: ")
                search_edge(graph, label1, label2)
            elif choice == "4":
                display_graph(graph)
            elif choice == "5":
                print("Exite the program...")
                break
            else:
                print("Invalid choice. Please try again.")

except FileNotFoundError:
    print("File not found:", filename)
