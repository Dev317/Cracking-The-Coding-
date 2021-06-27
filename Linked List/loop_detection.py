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
     
def check_loop(list_1):
    runner1 = list_1.head
    visit = []
    while runner1 != None:
        if runner1 not in visit:
            visit.append(runner1)
        else:
            return runner1.val
        runner1 = runner1.next
    return "No Loop"

list_1 = SingleLL()

list_1.head = Node("A")
list_1.size = 1
list_1.add(Node("B"))
list_1.add(Node("C"))

looped_node = Node("D")

list_1.add(looped_node)
list_1.add(Node("E"))
list_1.add(looped_node)

print(check_loop(list_1))