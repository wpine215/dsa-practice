class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self, node):
        self.root = node
        self.height = 1

    def insert(self, node):
        cursor = self.root
        while True:
            if node.value <= cursor.value:
                if cursor.left is not None:
                    cursor = cursor.left
                else:
                    cursor.left = node
                    break
            else:
                if cursor.right is not None:
                    cursor = cursor.right
                else:
                    cursor.right = node
                    break
    
    def search(self, value):
        cursor = self.root
        while True:
            if value == cursor.value:
                return cursor
            elif value <= cursor.value and cursor.left is not None:
                cursor = cursor.left
            elif value > cursor.value and cursor.right is not None:
                cursor = cursor.right
            else:
                return None

    def print(self):
        self.__print_recursive(self.root, 0)

    def __print_recursive(self, node, level, side=None):
        side_str = f"{side}: " if side is not None else ""
        print('-' * 2 * level + f"{side_str}{str(node.value)}")
        if node.left:
            self.__print_recursive(node.left, level + 1, "L")
        if node.right:
            self.__print_recursive(node.right, level + 1, "R")

def main():
    r = BinaryTreeNode(5)
    bt = BinaryTree(r)
    bt.insert(BinaryTreeNode(2))
    bt.insert(BinaryTreeNode(1))
    bt.insert(BinaryTreeNode(7))
    bt.insert(BinaryTreeNode(14))
    bt.insert(BinaryTreeNode(6))
    bt.print()

    print(bt.search(7), bt.search(7).value)
    print(bt.search(17))

if __name__ == "__main__":
    main()