from linkedList import Node, LinkedList

def reverse_list(list: LinkedList):
    if not list or not list.head:
        return # Nothing happens with empty list 
    cursor = list.head
    new_head = None
    while cursor:
        next = cursor.next
        cursor.next = new_head
        new_head = cursor
        cursor = next
    list.head = new_head

def merge_lists(a: LinkedList, b: LinkedList) -> LinkedList :
    c_a = a.head
    c_b = b.head
    head = Node(None) #create fake head
    tail = head
    while c_a or c_b:
        if not c_a or (c_b and c_a.data > c_b.data):
            tail.next = Node(c_b.data)
            c_b = c_b.next
        else:
            tail.next = Node(c_a.data)
            c_a = c_a.next
        tail = tail.next
    
    res = LinkedList()
    res.head = head.next # if something was merged - use first added element (except the fake head) as head
    return res

def merge_sort(list: LinkedList) -> LinkedList:
    n = list.count()
    if (n <= 1):
        return list
    
    cursor = list.head
    l_head = l_tail = Node(None)
    for i in range(n//2):
        l_tail.next = Node(cursor.data)
        l_tail = l_tail.next
        cursor = cursor.next
    left = LinkedList()
    left.head = l_head.next 

    r_head = r_tail = Node(None)
    while cursor:
        r_tail.next = Node(cursor.data)
        r_tail = r_tail.next
        cursor = cursor.next
    right = LinkedList()
    right.head = r_head.next 

    return merge_lists(merge_sort(left), merge_sort(right))


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)       
print('Початковий стан списку:')
llist.print_list()

reverse_list(llist)
print('Стан списку після виклику reverse_list:')
llist.print_list()


llist = merge_sort(llist)
print("Стан списку після виклику merge_sort:")
llist.print_list()

list_a = LinkedList()
list_b = LinkedList()
list_a.insert_at_end(1)
list_a.insert_at_end(2)
list_a.insert_at_end(7)
list_a.insert_at_end(9)
list_a.insert_at_end(12)
list_a.insert_at_end(15)
list_a.insert_at_end(18)
list_a.insert_at_end(21)
list_a.insert_at_end(25)

list_b.insert_at_end(0)
list_b.insert_at_end(2)
list_b.insert_at_end(3)
list_b.insert_at_end(4)
list_b.insert_at_end(5)
list_b.insert_at_end(6)
list_b.insert_at_end(7)
list_b.insert_at_end(8)
list_b.insert_at_end(10)
list_b.insert_at_end(20)
list_b.insert_at_end(30)
print("list_a:")
list_a.print_list()
print("list_b:")
list_b.print_list()
list_c = merge_lists(list_a, list_b)
print("merge_lists(list_a, list_b):")
list_c.print_list()

list_d = merge_lists(list_c, llist)
print("merge_lists(list_a, list_b, початковий)")
list_d.print_list()