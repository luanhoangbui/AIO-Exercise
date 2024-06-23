class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []
        
    def is_empty(self):
        return len(self.__stack) == 0
    
    def is_full(self):
        return len(self.__stack) == self.__capacity
    
    def push(self, value):
        if self.is_full():
            print('Stack is overflow')
        else:
            self.__stack.append(value)
    
    def pop(self):
        if self.is_empty():
            print('Stack is underflow')
        else:
            self.__stack.pop(-1)

    def top(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            return self.__stack[-1]
        
stack_1 = Stack(3)
stack_1.push(4)
stack_1.is_empty()
stack_1.pop()
stack_1.push(5)
stack_1.top()