from typing import List, Optional
from node import Node
from list_reverse import list_reverse
from stack import Stack
from queue import Queue
from stack_from_queues import StackFromQueues
from queue_from_stacks import QueueFromStacks

def list_from_array(array: List[int], n: int) -> Optional[Node]:
    """Converts a Python list of integers into a linked list."""
    first: Optional[Node] = None
    tail: Optional[Node] = None

    for i in range(n):
        node = Node(array[i])

        # If the list was empty, put the new node at the first
        if not first:
            first = node

        # Put the new node at the tail of the list
        if tail:
            tail.next = node
        tail = node

    return first


def list_print(first: Optional[Node]) -> None:
    """Prints the contents of a linked list, given its first node."""
    current: Optional[Node] = first

    if not current:
        print(" (null)", end="")

    while current:
        print(f" {current.value:4d}", end="")
        current = current.next
    print()


def list_free(first: Optional[Node]) -> None:
    """Frees the memory. In Python, we just break references.
    
    The garbage collector takes care of the actual deletion.
    """
    current: Optional[Node] = first
    while current:
        next_node = current.next
        current.next = None  # Unlink to help the GC
        current = next_node


def main():
    n: int = 16
    m: int = 8  # Retained to match C code, though unused in this snippet
    
    # In Python, we can just use a list comprehension instead of malloc
    array: List[int] = [i * i for i in range(n)]
    
    list_head: Optional[Node] = None

    print("\n===========================")
    print("== Testing list_reverse()")
    print("===========================\n")

    # Test 1: List created from array
    list_head = list_from_array(array, n)
    print("== Original list contents:", end="")
    list_print(list_head)
    
    list_head = list_reverse(list_head)
    print("== Reversed list contents:", end="")
    list_print(list_head)
    print()

    # Test 2: List of length 1
    # list_free(list_head)  # Python cleans this up when reassigned
    list_head = list_from_array([n], 1)
    print("== Original length=1 list contents:", end="")
    list_print(list_head)
    
    list_head = list_reverse(list_head)
    print("== Reversed length=1 list contents:", end="")
    list_print(list_head)
    print()

    # Test 3: Null list
    list_head = None
    print("== Original null list contents:", end="")
    list_print(list_head)
    
    list_head = list_reverse(list_head)
    print("== Reversed null list contents:", end="")
    list_print(list_head)
    print()

    # =============================================
    # == Testing queue-from-stacks implementation
    # =============================================
    print("\n=============================================")
    print("== Testing queue-from-stacks implementation")
    print("=============================================\n")
    
    qfs = QueueFromStacks()
    q = Queue()
    
    print("== Enqueueing into queue-from-stacks.")
    for i in range(n):
        val = 2 * i + 1
        qfs.enqueue(val)
        q.enqueue(val)

    print("== Dequeueing some from queue-from-stacks: front / dequeued (expected)")
    for _ in range(m):
        expected = q.dequeue()
        front = qfs.front()
        dequeued = qfs.dequeue()
        print(f"  - {front!s:>4} / {dequeued!s:>4} ({expected!s:>4})")

    print("== Enqueueing more into queue-from-stacks.")
    for i in range(n, n + m):
        val = 2 * i + 1
        qfs.enqueue(val)
        q.enqueue(val)

    print("== Dequeueing rest from queue-from-stacks: front / dequeued (expected)")
    while not q.is_empty():
        expected = q.dequeue()
        front = qfs.front()
        dequeued = qfs.dequeue()
        print(f"  - {front!s:>4} / {dequeued!s:>4} ({expected!s:>4})")

    print(f"== Is queue-from-stacks empty (expect 1)? {int(qfs.is_empty() or 0)}")


    # =============================================
    # == Testing stack-from-queues implementation
    # =============================================
    print("\n=============================================")
    print("== Testing stack-from-queues implementation")
    print("=============================================\n")
    
    sfq = StackFromQueues()
    s = Stack()
    
    print("== Pushing onto stack-from-queues.")
    for i in range(n):
        val = 2 * i
        sfq.push(val)
        s.push(val)

    print("== Popping some from stack-from-queues: top / popped (expected)")
    for _ in range(m):
        expected = s.pop()
        top = sfq.top()
        popped = sfq.pop()
        print(f"  - {top!s:>4} / {popped!s:>4} ({expected!s:>4})")

    print("== Pushing more onto stack-from-queues.")
    for i in range(n, n + m):
        val = 2 * i
        sfq.push(val)
        s.push(val)

    print("== Popping rest from stack-from-queues: top / popped (expected)")
    while not s.is_empty():
        expected = s.pop()
        top = sfq.top()
        popped = sfq.pop()
        print(f"  - {top!s:>4} / {popped!s:>4} ({expected!s:>4})")

    print(f"== Is stack-from-queues empty (expect 1)? {int(sfq.is_empty() or 0)}")


# Running the script
if __name__ == "__main__":
    main()
