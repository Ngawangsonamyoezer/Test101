class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        
        pass  

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_node(self, data_to_remove):
        current = self.head
        prev = None
        while current:
            if current.data == data_to_remove:
               
                if prev:
                    prev.next = current.next 
                else:
                    
                    self.head = current.next
                return  
            prev = current
            current = current.next

        print(f"Node with data {data_to_remove} not found in the linked list.")

    def sizeOfLL(self):
    
        pass  

    def printLL(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None") 


my_list = LinkedList()
my_list.insert(10)
my_list.insert(20)
my_list.insert(30)
my_list.printLL() 
my_list.remove_node(10)
my_list.printLL()
