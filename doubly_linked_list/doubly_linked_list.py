"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length = self.length + 1
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length = self.length + 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.head == None and self.tail == None:
            return None
        elif self.head == self.tail:
            old_head = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return old_head
        else:
            old_head = self.head
            old_head.next.prev = None
            self.head = old_head.next
            # self.head.prev = None
            self.length -= 1
            return old_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value, self.tail)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length = self.length + 1
        else:
            self.tail.next = new_node
            # new_node.prev = self.tail
            self.tail = new_node
            self.length = self.length + 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return None
        elif self.head == self.tail:
            removed_tail = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_tail
        else:
            removed_tail = self.tail
            removed_tail.prev.next = None
            self.tail = removed_tail.prev
            self.length -= 1
            return removed_tail

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.head == None and self.tail == None:
            return None 
        elif self.head == self.tail:
            return None
        elif self.head == node:
            return None
        else:
            self.add_to_head(node.value)
            self.delete(node)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.head == None and self.tail == None:
            return None
        elif self.head == self.tail:
            return None
        elif self.tail == node:
            return None
        else:
            self.add_to_tail(node.value)
            self.delete(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    # def delete(self, node):
    #     if self.head is None and self.tail is None:
    #         return None
    #     elif self.head == self.tail:
    #         self.head = None
    #         self.text = None
    #         self.length -= 1
    #     elif node == self.head:
    #         self.remove_from_head()
    #     elif node == self.tail:
    #         self.remove_from_tail()
    #     else:
    #         node.next.prev = node.prev
    #         node.prev.next = node.next
    #         self.length -= 1
    def delete(self, node):
        # pass
        # don't need to traverse; we have access to the `node`
        # check if DLL is empty
        if self.head is None and self.tail is None:
            return None
        # check if DLL has only 1 node
        elif self.head == self.tail:
            # set head and tail to None
            self.head = None
            self.tail = None
            # update length
            self.length -= 1
        # check if node is head 
        elif self.head == node:
            # run remove_from_head -- updated length
            DoublyLinkedList.remove_from_head(self)
        # check if node is tail
        elif self.tail == node:
            # run remove_from_tail -- updates length
            DoublyLinkedList.remove_from_tail(self)
        # othewise DLL has more than 1 node
        else:
            # redirect node's prev and next:
            # node's next points to its prev now `node.next.prev = node.prev`
            node.next.prev = node.prev 
            # node's prev points to its next now `node.prev.next = node.next`
            node.prev.next = node.next
            # update length
            self.length -= 1     

            

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if self.head == None and self.tail == None:
            return None
        else: 
            max = self.head.value
            current_head = self.head
            while current_head != None:
                if  current_head.value > max:
                    max = current_head.value 
                    current_head = current_head.next             
                else:
                    current_head = current_head.next
            return max
        return max


       
        
