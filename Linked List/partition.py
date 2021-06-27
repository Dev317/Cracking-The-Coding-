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

    def partition(self,num):
        curr_node = self.head
        temp_head = self.head
        runner = self.head
        
        #find head
        if self.head.val >= num:
            while curr_node.val >= num:
                curr_node = curr_node.next
                runner = runner.next
            self.head = curr_node
        else:
            while temp_head.val < num:
                temp_head = temp_head.next
                runner = runner.next

        temp = temp_head

        while temp.next.val != curr_node.val:
            temp = temp.next

        runner = runner.next

        while runner != None:
            if runner.val >= num:
                temp.next = runner
                temp = temp.next
            else:
                curr_node.next = runner
                curr_node = curr_node.next

            runner = runner.next
        
        curr_node.next = temp_head
        temp.next = None

           
list = SingleLL()
list.head = Node(6)
list.size = 1

list.add(Node(5))
list.add(Node(3))
list.add(Node(5))
list.add(Node(8))
list.add(Node(5))
list.add(Node(10))
list.add(Node(2))
list.add(Node(1))

print("Before: ")
list.print_list()

print("----\nAfter: ")
list.partition(5)
list.print_list()
