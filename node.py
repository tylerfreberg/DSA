#!/usr/bin/env python3

class SinglyLinkedList:
    def __init__(self):
        self._head = None

    class Node:
        def __init__(self, data, next_node = None):
            self._data = data
            self._next = next_node
    
        def data(self):
            return self._data

        def next(self):
            return self._next
    
        def has_next(self):
            return self._next is not None

        def append(self, next_node):
            self._next = next_node

    def insert_to_front(self, data):
        old_head = self._head
        self._head = Node(data, old_head)
        
    def insert_to_back(self, data):
        current = self._head
        if current is None:
            self._head = Node(data)
        else:
            while current.next is not None:
                current = current.next()
                current.append(Node(data))

    def _search(self, target):
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None

    def delete(self, target):
        current = self._head
        previous = None
        while current is not None:
            if current.data() == target:
                if previous is None:
                    self._head = current.next()
                else:
                    previous.append(current.next())
                return
            previous = current
            current = current.next()
        raise ValueError(f'No element with value {target} was found in the list.')

    def delete_from_front(self, target):
        if self._head is not None:
            data = self._head.data()
            self._head = self._head = current.next()
            return data
        else:
            return ValueError('Delete on an empty list.')

def main():
    pass

main()