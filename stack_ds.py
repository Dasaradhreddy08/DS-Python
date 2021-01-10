from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

    def reverse(self,val):
        while self.size()>0:
            self.pop()
        '''' self.container.clear()   - > works'''
        res=""
        for v in range(len(val)):
            self.push(val[v])

        for k in range(self.size()):
            res+=self.peek()
            self.pop()
        return res



s=Stack()

print(s.reverse("abcdef"))


