class MyQueue:
    def __init__(self, capacity):
        self . __capacity = capacity
        self . __queue = []

    def is_full(self):
        return len(self . __queue) == self . __capacity

    def enqueue(self, value):
        if self.is_full():
            print('Queue is overflow')
        else:
            self.__queue.append(value)

    def dequeue(self):
        if self.is_empty():
            print('Queue is underflow')
        else:
            self.__queue.pop(0)

    def front(self):
        # Your Code Here
        if len(self.__queue) == 0:
            print('Queue is empty')
        else:
            return self.__queue[0]
        # End Code Here


queue1 = MyQueue(capacity=5)
queue1 . enqueue(1)
assert queue1 . is_full() == False
queue1 . enqueue(2)
print(queue1 . front())
