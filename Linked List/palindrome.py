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

def reverse_ll(singlell):
    prev_node = None
    curr_node = singlell.head
        
    while curr_node != None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    singlell.head = prev_node
    return singlell     

def check_palindrome(list1):
    reverse = reverse_ll(list1)
    reverse.print_list()

    runner1 = list1.head
    runner2 = reverse.head

    while runner1 != None and runner2 != None:
        if runner1.val != runner2.val:
            return False

        runner1 = runner1.next
        runner2 = runner2.next        
    return True

list_1 = SingleLL()
list_1.head = Node(7)
list_1.size = 1
list_1.add(Node(6))
list_1.add(Node(1))
list_1.add(Node(6))
list_1.add(Node(7))

list_1.print_list()
print(check_palindrome(list_1))