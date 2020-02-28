
from doubly_linked_list import DoublyLinkedList


# overwrite oldest item in the buffer structure with the new item
# size is fixed - doesnt grow

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # overwrite oldest item in storage with new item
        if len(self.storage) > self.capacity:
            removed_node = self.storage.head
            self.storage.remove_from_head() # remove oldest item
            self.storage.add_to_tail(item)  # add new item - youngest
            if removed_node == self.current:
                self.current = self.storage.tail

        # Add is there still space to add in storage

        else if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head


    def get(self):
        # Note:  This is the only [] allowed

        list_buffer_contents = []

        ##
        list_buffer_contents.append(self.current.value)

        if self.current == self.storage.tail:
            node = self.storage.head
        else:
            node = self.current.next

        while node is not self.current:
            list_buffer_contents.append(node.value)
            if node.next:
                node = node.next
            else:
                node = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
