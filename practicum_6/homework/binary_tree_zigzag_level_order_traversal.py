from __future__ import annotations
from dataclasses import dataclass
from typing import Any

import yaml


@dataclass
class Node:
    key: Any
    data: Any = None
    left: Node = None
    right: Node = None


class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None

    def empty(self) -> bool:
        return self.root is None

    def zigzag_level_order_traversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = []
        res = []
        q.append(root)

        is_reversed = False
        while q:
            nodes_to_add = []
            values = []
            while q:
                node = q.pop()
                values.append(node.val)
                if is_reversed:
                    if node.right:
                        nodes_to_add.append(node.right)
                    if node.left:
                        nodes_to_add.append(node.left)
                else:
                    if node.left:
                        nodes_to_add.append(node.left)
                    if node.right:
                        nodes_to_add.append(node.right)
            if is_reversed:
                is_reversed = False
            else:
                is_reversed = True

            res.append(values)
            q = nodes_to_add
        
        return res



def build_tree(list_view: list[Any]) -> BinaryTree:
    bt = BinaryTree()
    node = Node(key=list[0])
    bt.root = node

    nodes = [node]
    for i, x in enumerate(list_view[1:]):
        if x is None:
            continue
        parent = nodes[i//2]
        new_node = Node(key=x)
        new_node.key = x
        if i % 2 == 0:
            parent.left = new_node
        else:
            parent.right = new_node
        nodes.append(new_node)

    return bt

if __name__ == "__main__":
    # Let's solve Binary Tree Zigzag Level Order Traversal problem from leetcode.com:
    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    # First, implement build_tree() to read a tree from a list format to our class
    # Second, implement BinaryTree.zigzag_traversal() returning the list required by the task
    # Avoid recursive traversal!

    with open(
        "practicum_6/homework/binary_tree_zigzag_level_order_traversal_cases.yaml", "r"
    ) as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        bt = build_tree(c["input"])
        zz_traversal = bt.zigzag_level_order_traversal(bt.root)
        print(f"Case #{i + 1}: {zz_traversal == c['output']}")
