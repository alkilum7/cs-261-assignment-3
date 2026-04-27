from __future__ import annotations
from typing import Optional
from node import Node

def list_reverse(first: Optional[Node]) -> Optional[Node]:
    """Reverses a singly-linked list in place with explicit type hints."""
    if first is None:
        return None
    prev: Node | None = None
    curr: Node = first
    next: Node
    while curr.next is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    curr.next = prev
    return curr