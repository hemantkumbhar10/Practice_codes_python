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

    def set_next(self, next_node):
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
        if (self.__head is None):
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        temp = self.__head
        while (temp is not None):
            t = temp.get_data()
            print(t)
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while (temp is not None):
            if temp is not None:
                return temp
            else:
                return None
            temp = temp.get_next

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while (temp is not None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


list1 = LinkedList()
list1.add("Sugar")
# Add all the required element(s)
# Search for the required node
node = list1.find_node("Sugar")
if (node != None):
    print("Node found")
else:
    print("Node not found")

print(Node.get_data(node))
