from collections import deque

class Queue:
    def __init__(self):
        self.buffer=deque()
    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        self.buffer.pop()

    def peek(self):
        return self.buffer[-1]

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


