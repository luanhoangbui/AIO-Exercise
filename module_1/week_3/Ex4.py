class Queue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

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
        if self.is_empty():
            print('Queue is empty')
        else:
            return self.__queue[0]


queue_1 = Queue(3)
queue_1.enqueue(1)
queue_1.enqueue(2)
queue_1.enqueue(3)

queue_1.front()
