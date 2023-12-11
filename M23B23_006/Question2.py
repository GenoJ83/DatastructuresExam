class StudentQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, student):
        self.queue.append(student)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


#Example

studentqueue = StudentQueue()

studentqueue.enqueue("Joshua")
studentqueue.enqueue("Alvin")
studentqueue.enqueue("Moses")



served_student = studentqueue.dequeue()
print(f"The first student to be served is: {served_student}")

is_empty = studentqueue.is_empty()
print(f"Is the queue empty? {is_empty}")


queue_size = studentqueue.size()
print(f"The current size of the queue is: {queue_size}")