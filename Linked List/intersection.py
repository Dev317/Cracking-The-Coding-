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
     
def check_intercept(list1, list2):
    visit = []

    runner1 = list1.head
    runner2 = list2.head

    while runner1 != None and runner2 != None:
        if runner1 in visit or runner2 in visit:
            return True
        else:
            visit.append(runner1)
            visit.append(runner2)
        runner1 = runner1.next
        runner2 = runner2.next
    
    while runner1 != None:
        if runner1 in visit:
            return True
        runner1 = runner1.next
    
    while runner2 != None:
        if runner2 in visit:
            return True
        runner2 = runner2.next
        
    return False

list_1 = SingleLL()
list_2 = SingleLL()

list_1.head = Node(7)
list_1.size = 1
list_1.add(Node(6))
list_1.add(Node(1))

intersect_node = Node(0)

list_1.add(intersect_node)
list_1.add(Node(4))

list_2.head = Node(5)
list_2.size = 1
list_2.add(Node(9))
list_2.add(Node(8))
list_2.add(Node(2))
list_2.add(Node(0))

list_2.add(intersect_node)

list_1.print_list()
list_2.print_list()

print(check_intercept(list_1, list_2))