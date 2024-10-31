import os 

def run_UnitTestDSAStack():
    os.system('python UnitTestDSAStack.py')

def run_UnitTestDSAQueue():
    os.system('python UnitTestDSAQueue.py')

def run_UnitTestDSALinkedList():
    os.system('python UnitTestDSALinkedList.py')

def run_UnitTestDSAHeap():
    os.system('python UnitTestDSAHeap.py')

def run_UnitTestDSAHashTable():
    os.system('python UnitTestDSAHashTable.py')

def run_UnitTestDSAGraph():
    os.system('python UnitTestDSAGraph.py')

def main_menu():
    while True:
        print("Main Menu:")
        print("1. test Stack")
        print("2. test Queue")
        print("3. test LinkedList")
        print("4. test Heap")
        print("5. test Hash")
        print("6. test Graph") 
        print("0. Exit")
        choice = input("Enter your choice (0-5): ")
        
        if choice == '1':
            run_UnitTestDSAStack()
        elif choice == '2':
            run_UnitTestDSAQueue()
        elif choice == '3':
            run_UnitTestDSALinkedList()
        elif choice == '4':
            run_UnitTestDSAHeap()
        elif choice == '5':
            run_UnitTestDSAHashTable()
        elif choice == '6':
            run_UnitTestDSAGraph()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

