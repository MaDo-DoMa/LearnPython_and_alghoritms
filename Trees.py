class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,value): #add value to the tree
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root,value)

    def _insert(self,node,value):
        #extra method to add tree like that smaller on left, bigger on right
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left,value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def find(self,value): #check if it's in tree
        return self._find(self.root,value)

    def _find(self,node,value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._find(node.left,value)
        else:
            return self._find(node.right,value)

    def inorder(self): #return in growing value
        result = []
        self._inorder(self.root,result)
        return result

    def _inorder(self,node,result):
        if node is not None:
            self._inorder(node.left,result)
            result.append(node.value)
            self._inorder(node.right,result)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(4)
    tree.insert(3)
    tree.insert(2)
    tree.insert(7)
    tree.insert(8)
    tree.insert(1)

    print(tree.inorder())