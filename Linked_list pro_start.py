class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data
    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next
    def set_next(self,next_node):
        self.__next = next_node

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head
    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if(self.__head is None):
            self.__head = self.__tail = new_node

        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        temp = self.__head
        while(temp is not None):
            print(temp.get_data())
            temp = temp.get_next()

obj = LinkedList()
obj.add("hemant")
obj.add('Kumbhar')
obj.add('hk')

obj.display()
