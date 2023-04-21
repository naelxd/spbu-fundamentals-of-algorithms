from __future__ import annotations
from dataclasses import dataclass
from typing import Any

import yaml
import ctypes
import copy
import gc

gc.disable()

@dataclass
class Element:
    key: Any
    data: Any = None
    np: int = 0

    def next(self, p_prev: int) -> int:
        return self.np ^ p_prev

    def prev(self, p_next: int) -> int:
        return self.np ^ p_next


class XorDoublyLinkedList:
    def __init__(self) -> None:
        self.head: Element = None
        self.tail: Element = None
        self.nodes = []

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        node_keys = []
        
        p_curr = id(self.head)
        p_prev = 0
        while p_curr:
            curr_el = self._get_element(p_curr)
            node_keys.append(str(curr_el.key))
            p_prev, p_curr = p_curr, curr_el.next(p_prev)
        
        return " <-> ".join(node_keys)

    def _get_element(self, p_id: int) -> Element:
        return ctypes.cast(p_id, ctypes.py_object).value

    def to_pylist(self) -> list[Any]:
        py_list = []

        p_curr = id(self.head)
        p_prev = 0
        while p_curr:
            curr_el = self._get_element(p_curr)
            py_list.append(curr_el.key)
            p_prev, p_curr = p_curr, curr_el.next(p_prev)

        return py_list

    def empty(self):
        return self.head is None

    def search(self, k: Element) -> Element:
        """Complexity: O(n)"""
        p_curr = id(self.head)
        curr_el = self.head
        p_prev = 0

        while p_curr:
            curr_el = self._get_element(p_curr)
            if curr_el.key == k.key:
                return curr_el
            p_prev, p_curr = p_curr, curr_el.next(p_prev)

        raise "No such index"


    def insert(self, x: Element) -> None:
        """Insert to the front of the list (i.e., it is 'prepend')
        Complexity: O(1)
        """

        if self.head is None:
            self.tail = x

        if self.head is not None:
            self.head.np = id(x) ^ self.head.np
            x.np = id(self.head)

        self.nodes.append(x)
        self.head = x


    def remove(self, x: Element) -> None:
        """Remove x from the list
        Complexity: O(1)
        """
        p_curr = id(self.head)
        p_prev = 0
        curr_el = self.head
        while p_curr and curr_el.key != x.key:
            p_prev, p_curr = p_curr, curr_el.next(p_prev)
            curr_el = self._get_element(p_curr)
        if p_curr:
            p_next = curr_el.next(p_prev)
            if p_prev:
                prev_el = self._get_element(p_prev)
                prev_el.np = prev_el.np ^ p_curr ^ p_next
            else:
                self.head = p_next
                prev_el = None

            if p_next:
                next_el = self._get_element(p_next)
                next_el.np = next_el.np ^ p_curr ^ p_prev
            else:
                self.tail = prev_el
            self.nodes.remove(curr_el)


    def reverse(self) -> XorDoublyLinkedList:
        """Returns the same list but in the reserved order
        Complexity: O(1)
        """
        self.head, self.tail = self.tail, self.head
        return self


if __name__ == "__main__":
    # You need to implement a doubly linked list using only one pointer
    # self.np per element. In python, by pointer, we understand id(object).
    # Any object can be accessed via its id, e.g.
    # >>> import ctypes
    # >>> a = ...
    # >>> ctypes.cast(id(a), ctypes.py_object).value
    # Hint: assuming that self.next and self.prev store pointers
    # define self.np as self.np = self.next XOR self.prev
    

    with open("practicum_6/homework/xor_list_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        l = XorDoublyLinkedList()
        for el in reversed(c["input"]["list"]):
            l.insert(Element(key=el))
        for op_info in c["input"]["ops"]:
            if op_info["op"] == "insert":
                l.insert(Element(key=op_info["key"]))
            elif op_info["op"] == "remove":
                l.remove(Element(op_info["key"]))
            elif op_info["op"] == "reverse":
                l = l.reverse()
        py_list = l.to_pylist()
        print(f"Case #{i + 1}: {py_list == c['output']}")
