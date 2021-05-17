class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if(self.__elements == self.__max_size -1):
            return True
        return False
        # Remove pass and write the logic to check whether Queue is full. If the queue is full, return true else return false.

    def enqueue(self, data):
        if(self.is_full()):
            print('Cant Insert,Queue is full')
        else:
            self.__rear +=1
            self.__elements[self.__rear] = data

    def is_empty(self):
        if(self.__elements == self.__front+1):
            return True
        return False

    def dequeue(self):
        if(self.is_empty()):
            print('Its already empty bitch')

        else:
            data = self.__elements[self.__front]
            self.__front +=1
            return data

    def display(self):
        index = self.__front
        while(index <= self.__rear):
            print(self.__elements[index])
            index +=1
        # Remove pass and write the logic to display all the queue element(s).

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__front
        while (index <= self.__rear):
            msg.append((str)(self.__elements[index]))
            index += 1
        msg = " ".join(msg)
        msg = "Queue data(Front to Rear): " + msg
        return msg


queue1 = Queue(5)
# Enqueue all the required element(s).
queue1.enqueue("Tom")
queue1.enqueue('jerry')
queue1.enqueue('hardy')
# Display all the elements in the queue.
queue1.display()
print('-----------------------------------------------')
print('-------------------DEQUEUE---------------------')
print('-----------------------------------------------')
print(queue1.dequeue())
