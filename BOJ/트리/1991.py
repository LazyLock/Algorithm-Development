import sys

n = int(sys.stdin.readline())
tree = {}

for _ in range(n):
    a, b, c = sys.stdin.readline().split()
    tree[a] = [b, c]

def preorder(s):
    if s != '.':
        print(s, end='')
        preorder(tree[s][0])
        preorder(tree[s][1])

def inorder(s):
    if s != '.':
        inorder(tree[s][0])
        print(s, end='')
        inorder(tree[s][1])

def postorder(s):
    if s != '.':
        postorder(tree[s][0])
        postorder(tree[s][1])
        print(s, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')