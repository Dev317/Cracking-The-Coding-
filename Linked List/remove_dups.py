class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None

class SingleLL:
    def __intit__(self):
        self.head = None

    def print_list(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node.val, end = "->")
            curr_node = curr_node.next
        print("NULL")

    def remove_dups(self):
        curr_node = self.head
        
        while curr_node.next != None:
            running_node = curr_node.next
            prev_node = curr_node

            while running_node != None:
                if running_node.val != curr_node.val:
                    prev_node = running_node
                    running_node = running_node.next
                else:
                    prev_node.next = running_node.next
                    running_node = running_node.next
            
            curr_node = curr_node.next





list = SingleLL()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Mon")
e5 = Node("Thurs")
e6 = Node("Mon")
e7 = Node("Wed")
e8 = Node("Fri")

# Link first Node to second node
list.head.next = e2

# Link the rest
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7
e7.next = e8

list.print_list()

list.remove_dups()
list.print_list()
