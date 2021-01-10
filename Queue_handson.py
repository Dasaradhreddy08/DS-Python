from Queue import Queue

q = Queue()

for val in range(6):
    q.enqueue(val + 1)
print(q.size())
print(q.peek())

print(q.dequeue())
print(q.is_empty())
print(q.size())
print(q.peek())

for val in range(2):
    q.dequeue()
    print(q.size())


