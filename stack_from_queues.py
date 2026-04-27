"""
Stack implemented using two queues.

This module assumes a Queue class with: enqueue(int), dequeue()->int, front()->int, is_empty()->bool, clear()->None.
"""

from __future__ import annotations
from queue2 import Queue

class StackFromQueues:
    """
    A LIFO stack implemented using two FIFO queues.
    
    At any time, **exactly one** of q1 or q2 holds all the elements; the other is empty.
    Push appends to the non-empty queue.
    Top/Pop shift elements to expose/remove the most-recently-pushed value.
    """

    q1: Queue
    q2: Queue

    def __init__(self) -> None:
        # initialize/create the stack from queues
        self.q1 = Queue()
        self.q2 = Queue()

    def is_empty(self) -> bool:
        return self.q1.is_empty() and self.q2.is_empty()

    def push(self, value: int) -> None:
        self._active_and_passive()[0].enqueue(value)

    def _active_and_passive(self):
        if self.q1.is_empty():
            return (self.q2, self.q1)
        else:
            return (self.q1, self.q2)

    def top(self) -> int:
        return_value = self.pop()
        self.push(return_value)
        return return_value

    def pop(self) -> int:
        assert not self.is_empty()
        (active_queue, inactive_queue) = self._active_and_passive()
        return_value: int
        while True:
            return_value = active_queue.dequeue()
            if active_queue.is_empty():
                return return_value
            inactive_queue.enqueue(return_value)

    def clear(self) -> None:
        self.q1 = None # type: ignore
        self.q2 = None # type: ignore