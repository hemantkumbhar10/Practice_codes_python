class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if(self.__top + 1 == self.__max_size):
            return True
        return False
        # Remove pass and write the logic to check whether stack is full. If the stack is full, return true else return false.

    def push(self, data):
        if(self.is_full() is False):
            self.__top += 1
            self.__elements[self.__top] = data
        else:
            print('Cant insert more,Stack is full')

    def display(self):
        index = self.__top
        while(index >= 0):
            print(self.__elements[index])
            index -=1

    def is_empty(self):
        if(self.__top == -1):
            return True
        return False

    def pop(self):
        if(self.is_empty()):
            print('Stack is empty')
        else:
            index = self.__top
            data = self.__elements[index]
            index -=1
            return  data



    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__top
        while (index >= 0):
            msg.append((str)(self.__elements[index]))
            index -= 1
        msg = " ".join(msg)
        msg = "Stack data(Top to Bottom): " + msg
        return msg


stack1 = Stack(5)
# Push all the required element(s).
stack1.push('t')
stack1.display()
print(stack1.pop())
print(stack1.pop())

