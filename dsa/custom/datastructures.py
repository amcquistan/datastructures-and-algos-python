
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"<Node: data={self.data}>"


class LinkedList:
    head = None
    current = None
    size = 0

    def __init__(self):
        self.items = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.head is None:
            raise StopIteration

        if self.current is None:
            self.current = self.head
            return self.current.data

        if self.current.next is not None:
            self.current = self.current.next
            return self.current.data

        self.current = None
        raise StopIteration

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if not self.head:
            raise IndexError

        if index >= self.size or index < 0:
            raise IndexError

        i = 0
        curr = self.head
        while curr.next or i == index:
            if i == index:
                return curr.data
            curr = curr.next
            i += 1

    def __setitem__(self, index, value):
        if index >= self.size or index < 0:
            raise IndexError

        i = 0
        curr = self.head
        while curr.next or i == index:
            if i == index:
                curr.data = value
                break
            curr = curr.next
            i += 1


    def add(self, value, index=None):
        """Adds an element to the linked list.
        
        Args:
          value (any): the data value to add to the linked list.
          index (int): optionally specify the index to add this value at.
        """
        node = Node(value)
        if index is not None:
            if index > self.size:
                raise IndexError
            else:
                if index == 0:
                    node.next = self.head
                    self.head = node
                else:
                    prev = self.head
                    curr = self.head.next
                    i = 0
                    while curr.next and i != index:
                        prev = curr
                        curr = curr.next
                        i += 1

                    prev.next = node
                    node.next = curr
        elif self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

        self.size += 1

    def clear(self):
        """Clears all elements from linked list."""
        self.head = None
        self.size = 0

    def index(self, value) -> int:
        """Finds the index of the first element matching the passed in value.

        Args:
          value (any): the data value to lookup from the linked list.

        Returns:
          int: the index of the value in the linked list or -1 if not present.
        """
        i = -1
        if not self.head:
            return i

        curr = self.head
        while curr.next or curr.data == value:
            i += 1
            if curr.data == value:
                return i
            curr = curr.next

        return -1

    def empty(self) -> bool:
        """Checks to see if linked list contains elements.

        Returns:
          bool: True if empty, False otherwise
        """
        return self.size == 0

    def remove(self, value) -> bool:
        """Removes the first element that matches value.

        Args:
          value (any): the data value to remove from the linked list.

        Returns:
          bool: True if value is removed, False otherwise
        """
        removed = False
        if not self.head:
            return removed

        if self.head.data == value:
            self.head = self.head.next
            removed = True
        else:
            curr = self.head
            while curr.next and curr.next.data != value:
                curr = curr.next
            if curr.next:
                curr.next = curr.next.next
                removed = True

        if removed:
            self.size -= 1

        return removed

    def reverse(self):
        """Reverses the order of the elements within the linked list"""
        if not self.head or not self.head.next:
            return

        next_head = self.head.next
        self.head.next = None
        while next_head:
            next_next = next_head.next
            next_head.next = self.head
            self.head = next_head
            next_head = next_next

    def __str__(self):
        items = []
        curr = self.head
        while curr.next:
            items.append(curr)
            curr = curr.next

        items.append(curr)

        items = ', '.join([str(x) for x in items])
        return f'<LinkedList: items=[{items}]>'


class Stack:

    def __init__(self):
        self._ll = LinkedList()

    def __len__(self):
        return len(self._ll)

    def clear(self):
        """Clears the stack, emptying all elements from it."""
        self._ll.clear()

    def peek(self):
        """Retrieves but does not remove the top element of the stack."""
        return self._ll[0]

    def pop(self):
        """Removes the top element from the stack."""
        item = self._ll[0]
        self._ll.remove(item)
        return item

    def push(self, value):
        """Adds element to top of stack.

        Args:
          value (any): the data value to push on the top of the stack.
        """
        self._ll.add(value, index=0)


class Queue:

    def __init__(self):
        self._ll = LinkedList()

    def __len__(self):
        return len(self._ll)

    def add(self, value):
        """Add element to back of queue"""
        self._ll.add(value)

    def clear(self):
        """Clears the queue, emptying all elements from it."""
        self._ll.clear()

    def peek(self):
        """View first element of queue"""
        return self._ll[0]

    def pop(self):
        """Remove element from top (start) of queue"""
        item = self._ll[0]
        self._ll.remove(item)
        return item
