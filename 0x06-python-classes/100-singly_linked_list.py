#!/usr/bin/python3
"""Defines a Node and a SinglyLinkedList classes"""


class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
        data (int): The data value of the node.
        next_node (Node or None): The next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance.

        Args:
            data (int): The data value of the node.
            next_node (Node or None, optional): The next node in the linked list. Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data value of the node.

        Returns:
            int: The data value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data value of the node.

        Args:
            value (int): The new data value of the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
            Node or None: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node or None): The new next node in the linked list.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head (Node or None): The head node of the linked list.
    """

    def __init__(self):
        """
        Initializes a SinglyLinkedList instance with an empty linked list.
        """
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        current = self.__head
        result = ""
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip("\n")

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the linked list (increasing order).

        Args:
            value (int): The data value of the new Node to be inserted.
        """
        new_node = Node(value)

        if not self.__head or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
