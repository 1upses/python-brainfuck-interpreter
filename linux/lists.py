import numpy as np

class list:
    def __init__(self):
        self.list = np.array([], dtype=int)
        self.length = 0

    def add(self, data):
        self.list = np.append(self.list, data)
        self.length += 1
    
    def increment(self, index):
        error_handling(self, index)
        self.list[index] += 1

    def decrement(self, index):
        error_handling(self, index)
        self.list[index] -= 1

    def get(self, index):
        error_handling(self, index)
        return self.list[index]
    
    def set(self, index, data):
        error_handling(self, index)
        self.list[index] = data

    def show(self):
        print(self.list)

def error_handling(list, index):
    if index < 0:
        raise IndexError("Index out of range")
    while index >= list.length:
        list.add(0)
