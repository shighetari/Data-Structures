class Node:
    def __init__(self, value, next_node=None):
        # the value that the node is holding
        self.value = value
        # reference to the next node in the linked list
        self.next_node = next_node

    # Method to get the value of the node
    def get_value(self):
        self.value
    # Method to get the node's `next_node`

    def get_next(self):
        self.next_node
    # Method to update the node's value `next_node`

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap the value in a node
        new_node = Node(value)
        # check if Linked List is empty
        if self.head is None and self.tail is None:
            # set head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise, the list has at least one node
        else:
            # update the last node's `next_node` to the new node
            self.tail.set_next(new_node)
            # update `self.tail` to point the new node we just added
            self.tail = new_node

    def remove_tail(self):
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            return None

        # check if the linked list has only one node
        if self.head == self.tail:
            # store the node we're going to remove's value
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

            # otherwise, the linked list has more than one Node
            # store the last node's value in another variable so we can return it
            val = self.tail.get_value()
            # we need to set `self.tail` to the second-to-last node
            # the only way we cand o this, is by traversing the whole linked list from the beginning
            # starting from the head, we'll traverse down to the second-to-last Node
            # init another reference to keep track of where we are in the linked
            # ^ lists as we're iterating
            current = self.head

            # keep iterating until the node after `current` is after tail
            while current.get_next() != self.tail:
                # keep iterating
                current = current.get_next()

            # set `self.tail` to `current`
            self.tail = current
            # set the new tail's `next_node` to  None
            self.tail.set_next(None)
            return val

    def remove_head(self):
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            return None
        # check if there is only one linked list node
        if self.head == self.tail: 
            val = self.head.get_value()
            self.head = None
            self.tail = None
        else: 
            # store the old head's value that we need to return
            val = self.head.get_value()
            # set `self.head` to the old head's `next_node`
            self.head = self.head.get_next()
            # return the old_head's value
            return val


ll = LinkedList()
ll.add_to_tail(5)

# ll = Node(5)
# 11.set_next((7))
# ll.next_node.set_next((Node18))
