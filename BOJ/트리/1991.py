import sys


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def preorder(node):
    if node is None:
        return
    print(node.data, end='')
    preorder(tree[node.left])
    preorder(tree[node.right])


def inorder(node):
    if node is None:
        return
    inorder(tree[node.left])
    print(node.data, end='')
    inorder(tree[node.right])


def postorder(node):
    if node is None:
        return
    postorder(tree[node.left])
    postorder(tree[node.right])
    print(node.data, end='')


n = int(sys.stdin.readline())
tree = {'.': None}

for _ in range(n):
    a, b, c = sys.stdin.readline().split()
    tree[a] = Node(a, b, c)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])