class Node:

    def __init__(self,data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data
    def get_next(self):
        return self.__next
    def set_next(self,next):
        self.__next = next

class LinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None

    def add(self, data):
        new_data = Node(data)
        if(self.__head == None):
            self.__head = self.__tail = new_data
        else:
            self.__tail.set_next(new_data)
            self.__tail = new_data

    def display(self):
        node = self.__head
        while(node is not None):
            if(node.get_data() is not None):
                print(node.get_data())
            node = node.get_next()

    def find_node(self, data):
        node = self.__head
        while(node is not None):
            if(node.get_data() == data):
                return node
            node = node.get_next()
        return None

    def insert_node(self, data, data_before):
        new_node = Node(data)
        if(data_before == None):
            new_node.set_next(self.__head)
            self.__head = new_node
            if(new_node.get_next() == None):
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() == None):
                    self.__tail = new_node

    def delete_node(self, data):
        del_node = self.find_node(data)
        if(del_node is not None):
            if(del_node == self.__head):
                if(self.__head != self.__tail):
                    self.__head = del_node.get_next()
                else:
                    self.__head = self.__tail = None

            else:
                temp = self.__head
                while(temp is not None):
                    if(temp.get_next() == del_node):
                        temp.set_next(del_node.get_next())
                        if(del_node == self.__tail):
                            self.__tail = None
                    temp = temp.get_next()
        else:
            print(data, 'not found so i cant delete it bitch')
            

lst = LinkedList()
lst.add('monitor')
lst.add('keyboard')
lst.add('mouse')
lst.add('touchpad')
#lst.insert_node('usb', 'mouse')
#print(lst.find_node('keyboard'))
lst.delete_node('touchpad')
lst.display()