
"""
This module contains the definition of a Queue class implementing
a simple queue using a singly-linked list of Node objects.
"""

from __future__ import annotations
from typing import Optional
from node import Node


class Queue:
    """
    A FIFO queue implemented via a singly-linked list.
    Maintains pointers to the first (front) and last (rear) nodes.
    """
    
    def __init__(self) -> None:
        # Equivalent to queue_create(): start with an empty queue.
        self.first: Optional[Node] = None
        self.last: Optional[Node] = None

    def is_empty(self) -> bool:
        """
        Returns True if the queue has no elements.
        """
        return self.first is None
        
    def enqueue(self, value: int) -> None:
        """
        Appends a new node with the given value at the rear of the queue.
        """        
        new_node = Node(value)

        # Link the current last to the new node (if a last exists).
        if self.last is not None:
            self.last.next = new_node

        # Update last to the new node.
        self.last = new_node

        # If the queue was empty, first also points to the new node.
        if self.first is None:
            self.first = new_node
            
    def front(self) -> int:
        """
        Returns the value at the front of the queue without removing it.
        
        Raises:
        AssertionError if the queue is empty.
        """
        assert self.first is not None, "front() called on empty queue"
        return self.first.value
                    
    def dequeue(self) -> int:
        """
        Removes and returns the value at the front of the queue.
        
        Raises:
        AssertionError if the queue is empty.
        """
        assert self.first is not None, "dequeue() called on empty queue"
        
        # Remove the front node and remember its value.
        dequeued_first = self.first
        value = dequeued_first.value
        self.first = dequeued_first.next
        
        # If the dequeued node was also the last, queue becomes empty.
        if self.first is None:
            self.last = None
            
        # Break the link to help GC (optional, but mirrors explicit free semantics).
        dequeued_first.next = None
        return value
        
    def clear(self) -> None:
        """
        Iteratively dequeues all elements to break links.
        (Python's garbage collector handles memory management automatically.)
        """
        while not self.is_empty():
            self.dequeue()
