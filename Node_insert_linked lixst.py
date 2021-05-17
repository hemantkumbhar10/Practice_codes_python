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
            if (temp.get_data() == data):
                return temp
            temp = temp.get_next()
        return None

    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head = new_node
            if(new_node.get_next()==None):
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if (node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if (new_node.get_next() is None):
                    self.__tail = new_node

    def delete(self, data):
        node = self.find_node(data)
        if (node is not None):
            if (node == self.__head):
                if (self.__head != self.__tail):
                    self.__head = node.get_next()
                else:
                    self.__head = self.__tail = None

            else:
                temp = self.__head
                while(temp is not None):
                    if(temp.get_next() == node):
                        temp.set_next(node.get_next())
                        if(node == self.__tail):
                            self.__tail = temp
                        node.set_next(None)
                    temp = temp.get_next()

        else:
            print(data, 'is not found')



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
# Add all the required element(s)
list1.add('water')
list1.add('salt')
list1.add('Sugar')
list1.add('chilli')
# Insert the element in the required position
list1.insert("NewIte"
             "", 'Sugar')
'''#list1.display()
#list1.find_node('salt')
list1.delete('water')'''
list1.display()
