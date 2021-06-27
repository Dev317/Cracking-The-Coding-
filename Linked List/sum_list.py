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

def sum_list(singlell_1, singlell_2):
    # 7 -> 1 -> 6
    # 5 -> 9 -> 2
    count_1 = 0
    count_2 = 0
    final_singlell = SingleLL()
    final_singlell.size = 0

    carry = False
    runner_1 = singlell_1.head
    runner_2 = singlell_2.head
    while count_1 < singlell_1.size and count_2 < singlell_2.size:
        temp_sum = runner_1.val + runner_2.val
        if carry:
            temp_sum  += 1
        
        if temp_sum >= 10:
            temp_sum %= 10
            carry = True
        else:
            carry = False
        
        if final_singlell.size == 0:
            final_singlell.head = Node(temp_sum)
            final_singlell.size = 1
        else:
            final_singlell.add(Node(temp_sum))

        runner_1 = runner_1.next
        runner_2 = runner_2.next
        count_1 += 1
        count_2 += 1
    
    if singlell_1.size == singlell_2.size:
        if carry:
            final_singlell.add(Node(1))
        return final_singlell
    else:
        while count_1 < singlell_1.size:
            temp_sum = runner_1.val
            if carry:
                temp_sum += 1
            
            if temp_sum >= 10:
                temp_sum %= 10
                carry = True
            else:
                carry = False
            final_singlell.add(Node(temp_sum))
            runner_1 = runner_1.next
            count_1 += 1

        while count_2 < singlell_2.size:
            temp_sum = runner_2.val
            if carry:
                temp_sum += 1
            
            if temp_sum >= 10:
                temp_sum %= 10
                carry = True
            else:
                carry = False
            final_singlell.add(Node(temp_sum))
            runner_2 = runner_2.next
            count_2 += 1

        return final_singlell

print("Backward Case:")
list_1 = SingleLL()
list_1.head = Node(7)
list_1.size = 1
list_1.add(Node(1))
list_1.add(Node(6))

list_2 = SingleLL()
list_2.head = Node(5)
list_2.size = 1
list_2.add(Node(9))
list_2.add(Node(2))

print("Before: ")
list_1.print_list()
list_2.print_list()

print("----\nAfter: ")
final = sum_list(list_1, list_2)
final.print_list()



print("\n\nForward Case:")
list_3 = SingleLL()
list_3.head = Node(6)
list_3.size = 1
list_3.add(Node(1))
list_3.add(Node(7))

list_4 = SingleLL()
list_4.head = Node(2)
list_4.size = 1
list_4.add(Node(9))
list_4.add(Node(5))

print("Before: ")
list_3.print_list()
list_4.print_list()

print("----\nAfter: ")
list_3 = reverse_ll(list_3)
list_4 = reverse_ll(list_4)
final = sum_list(list_3, list_4)
final = reverse_ll(final)
final.print_list()