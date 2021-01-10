from Queue import Queue

q1=Queue()

q1.enqueue({"company":"Walmart","timestamp":"15 apr, 11.01 AM","price":131.10})
q1.enqueue({"company":"Walmart","timestamp":"15 apr, 11.03 AM","price":132.30})
q1.enqueue({"company":"Walmart","timestamp":"15 apr, 11.05 AM","price":132.05})

print(q1.buffer)


print(q1.peek())
q1.dequeue()

print(q1.peek())