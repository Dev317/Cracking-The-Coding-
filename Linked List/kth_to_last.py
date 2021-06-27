class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SingleLL:
    def __intit__(self):
        self.head = None
        self.size = 0
    
    def add(self, node):
        if self.head == None:
            self.head = node
        else:
            curr_node = self.head
            while curr_node.next != None:
                curr_node = curr_node.next
            
            curr_node.next = node

        self.size += 1
            

    def print_list(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node.val, end = "->")
            curr_node = curr_node.next
        print("NULL")

    def return_kth_to_last(self,num):
        counter = -self.size
        curr_node = self.head
        while num != -counter:
            counter += 1
            curr_node = curr_node.next
        return curr_node.val


list = SingleLL()
list.head = Node("Mon")
list.size = 1

list.add(Node("Tue"))
list.add(Node("Wed"))
list.add(Node("Mon"))
list.add(Node("Thurs"))
list.add(Node("Mon"))
list.add(Node("Wed"))
list.add(Node("Fri"))

list.print_list()
print(list.size)

print(list.return_kth_to_last(3))
