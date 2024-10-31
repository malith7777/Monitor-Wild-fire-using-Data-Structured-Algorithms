from DSALinkedList import DSALinkedList
from DSALinkedList import DSALinkedListIterator
class DSAQueue:
    def __init__(self):
        self.list = DSALinkedList()

    def enqueue(self, value): # Adds an element to the end of the queue
        self.list.insert_last(value)

    def dequeue(self): # Removes and returns the element at the front of the queue
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.list.remove_first()

    def peek(self): # Returns the element at the front of the queue without removing it
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.list.peek_first()

    def is_empty(self): # Checks if the queue is empty
        return self.list.is_empty()

    def __iter__(self): # Returns an iterator over the elements in the queue, in the order they would be dequeued
        return iter(self.list)
