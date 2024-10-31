from DSALinkedList import DSALinkedList
from DSALinkedList import DSALinkedListIterator
class DSAStack:

    def __init__(self):
        self.list = DSALinkedList()  # initialize the linked list

    def push(self, value):  # Pushes an element onto the top of the stack.
        self.list.insert_first(value)  # add the value to the front of the linked list

    def pop(self):  # Removes and returns the element at the top of the stack.
        if self.isEmpty():
            raise ValueError("Stack is empty")
        return self.list.remove_first()  # remove and return the first element in the linked list

    def peek(self):  # Returns the element at the top of the stack without removing it.
        if self.isEmpty():
            raise ValueError("Stack is empty")
        return self.list.peek_first()  # return the first element in the linked list without removing

    def isEmpty(self):  # Determines if the stack is empty.
        return self.list.is_empty()

    def __iter__(self): # Returns an iterator over the elements in the stack.
        return iter(self.list) # return an iterator over the linked list.
