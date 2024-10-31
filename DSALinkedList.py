class DSALinkedList:
    class DSAListNode:
        def __init__(self, inValue):
            self.value = inValue
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return False

    def insert_first(self, inValue):
        new_node = DSALinkedList.DSAListNode(inValue)
        if self.is_empty():
            self.tail = new_node
        else:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, inValue):
        new_node = DSALinkedList.DSAListNode(inValue)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node

    def peek_first(self):
        if self.is_empty():
            raise ValueError("List is empty")
        return self.head.value

    def peek_last(self):
        if self.is_empty():
            raise ValueError("List is empty")
        return self.tail.value

    def remove_first(self):
        if self.is_empty():
            raise ValueError("List is empty")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return value

    def remove_last(self):
        if self.is_empty():
            raise ValueError("List is empty")
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return value

    def __iter__(self):
        return DSALinkedListIterator(self)

class DSALinkedListIterator:
    def __init__(self, the_list):
        self.next_node = the_list.head

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_node is None:
            raise StopIteration
        value = self.next_node.value
        self.next_node = self.next_node.next
        return value

    def __str__(self):
        sb = []
        for item in self:
            sb.append(str(item))
            sb.append(" ")
        return "".join(sb).strip()
