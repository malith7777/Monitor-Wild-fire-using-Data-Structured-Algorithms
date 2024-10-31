import os

def run_task1():
    os.system('python task1.py')

def run_graph():
    os.system('python graph.py')

def run_Hashtable():
    os.system('python Hashtable.py')

def run_heap():
    os.system('python heap.py')

def run_iter():
    os.system('python iter.py')

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Run task1")
        print("2. Run graph")
        print("3. Run Hashtable")
        print("4. Run heap")
        print("5. Run iter")
        print("0. Exit")
        choice = input("Enter your choice (0-5): ")
        
        if choice == '1':
            run_task1()
        elif choice == '2':
            run_graph()
        elif choice == '3':
            run_Hashtable()
        elif choice == '4':
            run_heap()
        elif choice == '5':
            run_iter()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

