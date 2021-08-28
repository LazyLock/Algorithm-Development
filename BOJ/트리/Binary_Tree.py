class Node:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class binary_Tree:
    def __init__(self):
        self.root = None

    def search(self, key):
        p = self.root
        while True:
            if p is None:
                return False
            if key == p.key:
                return p.value
            elif key > p.key:
                p = p.right
            else:
                p = p.left

    def add(self, key, value):

        def add_node(node, key, value):
            if node.key == key:
                return False
            elif node.key < key:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            else:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key):
        p = self.root
        parent = None
        is_left_child = True

        while True:  #제거될 위치에 p를 갖다놓음.
            if p is None:
                return False
            if key == p.key:
                break
            else:
                parent = p
                if p.key > key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right

        if p.left is None:  #  p의 왼쪽 자식이 없을 경우(오른쪽 자식 하나이거나 둘다 없거나)
            if p == self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right

        elif p.right is None:  #  p의 오른쪽 자식이 없을 경우(왼쪽 자식 하나이거나 둘다 없거나)
            if p == self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left

        else:  #  p에게 자식 노드가 두개 있을 경우, p의 자식 중 가장 큰 값을 p의 자리로 가져옴
            parent = p
            left = p.left
            is_left_child = True

            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False

            p.value = left.value
            p.key = left.key
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left