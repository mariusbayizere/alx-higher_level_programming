#!/usr/bin/python3
"""Define a class Square."""


class Node:
    """
    Node class for a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        initialization called when instance of class created
        """
        if self.validate_data(data):
            self.__data = data
        if self.validation_Node(next_node):
            self.__next_node = next_node

    @property
    def data(self):
        """
        get the data attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        set the data attribute
        """
        if self.validate_data(value):
            self.__data = value

    @property
    def next_node(self):
        """
        get the node attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        set the node attribute
        """
        if self.validation_Node(value):
            self.__next_node = value

    def validate_data(self, data):
        """
        validates the data, checking its type
        Returns true or false if valid or not respectively
        """
        if isinstance(data, int):
            return True
        return False

    def validation_Node(self, node):
        """
        validates the node, checking it's a node object
        Returns true or false if valid or not respectively
        """
        if isinstance(node, Node) or node is None:
            return True
        return False


class SinglyLinkedList:
    """
    contains nodes for a singly linked list and methods for ->
    insertion
    """
    def __init__(self):
        """
        initialize called when object of class created
        """
        self.__head = None

    def __str__(self):
        """
        used by print to display linked list
        """
        current = self.__head
        string = ""
        while current is not None:
            string += str(current.data)
            current = current.next_node
            if current is not None:
                string += '\n'
        return string

    def sorted_insert(self, value):
        """
        inserts a new Node into the correct sorted position
                                            (based on data)
        """
        current = self.__head
        if current is None:
            self.__head = Node(value)
            return

        prev = None
        while current is not None:
            if (current.next_node is None or current.next_node.data >= value):
                if (current.data >= value):
                    next_n = current
                    current = Node(value)
                    current.next_node = next_n
                    if prev is not None:
                        prev.next_node = current
                    else:
                        self.__head = current
                else:
                    next_n = current.next_node
                    current.next_node = Node(value)
                    current.next_node.next_node = next_n
                return

            prev = current
            current = current.next_node
