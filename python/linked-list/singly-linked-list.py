class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    # def add_empty(self, data):
    #     if self.head is None:
    #         new_node = Node(data)
    #         self.head = new_node
    #     else:
    #         print("Linked list is not empty!")
            
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
    def add_after_node(self, data, x):
        if self.head is None:
            print("Linked list is empty!")
            return
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("The node doesn't exist")
        else:
            new_node = Node(data)
            new_node.ref = n.ref 
            n.ref = new_node
        
    def add_before_node(self, data, x):
        if self.head is None:
            print("Linked list is empty!")
            return
        n = self.head
        while n is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n is None:
            print("The node doesn't exist")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def delete_begin(self):
        if self.head is None:
            print("Linked list is emptY!")
        else:
            self.head = self.head.ref
            
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    
    def delete_element(self, x):
        if self.head is None:
            print("Linked list is emptY!")
        else:
            n = self.head
            while n is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n is None:
                print("The element doesn't exist")
                return
            n.ref = n.ref.ref

    
    def traverse_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end = " --> ")
                n = n.ref
            print("None", end = "")

    
        
LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_end(40)
LL1.add_before_node(50, 40)
LL1.add_after_node(60, 20)
LL1.delete_begin()
LL1.delete_element(50)
LL1.add_end(80)
LL1.add_end(70)
LL1.delete_end()
LL1.delete_end()

LL1.traverse_LL()        

        