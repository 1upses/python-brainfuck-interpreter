class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, data):
        if self.head == None:
            self.head = node(data)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node(data)
        self.length += 1
    
    def increment(self, index):
        error_handling(self, index)
        current = self.head
        for _ in range(index):
            current = current.next
        current.data += 1

    def decrement(self, index):
        error_handling(self, index)
        current = self.head
        for _ in range(index):
            current = current.next
        current.data -= 1

    def get(self, index):
        error_handling(self, index)
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    
    def set(self, index, data):
        error_handling(self, index)
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def show(self):
        current = self.head
        while current != None:
            print(current.data, end=", ")
            current = current.next

def error_handling(list, index):
    if index < 0:
        raise IndexError("Index out of range")
    while index >= list.length:
        list.add(0)
