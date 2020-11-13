class Tree:
    def __init__(self):
        self.left_node = None
        self.right_node = None
        self.tree = None

class BST(Tree):
    def __init__(self, number: int):
        self.root = number

    def insert(self, num: int):
        if num < self.root:
            if self.left_node is not None:
                self.left_node.insert(num=num)
            else:
                self.left_node = BST(number=num)
        elif num > self.root:
            if self.right_node is not None:
                self.right_node.insert(num=num)
            else:
                self.right_node = BST(number=num)

        return

    def remove(self, num: int):
        if num < self.root:
            if self.left_node is not None:
                self.left_node.remove(num=num)
        elif num > self.root:
            if self.right_node is not None:
                self.right_node.remove(num=num)
        else:
            if self.left_node is not None:
                self.root = self.left_node.root
                left = self.left_node.left_node
                right = self.left_node.right_node
                
                if self.right_node is not None:
                    self.left_node = left
                else:
                    self.right_node = right
        return

    def dfs(self, num: int) -> BST:
        if self.root == num:
            return self
        elif self.root < num:
            self.right_node.dfs(num=num)
        elif self.root > num:
            self.left_node.dfs(num=num)
        else:
            return None

    def balance(self, init_num: int = None):
        if init_num is None:
            if self.left_node is not None:
                num = self.left_node.balance()

                if num > self.root:
                    self.balance(init_num=num)
            if self.right_node is not None:
                num = self.right_node.balance()

                if num < self.root:
                    self.balance(init_num=num)
        else:
            if init_num < self.root:
                if self.left_node is not None:
                    num = self.left_node.balance(init_num=init_num)
                else:
                    self.left_node.root = init_num
                    self.right_node = self.right_node.right_node
            elif init_num > self.root:
                if self.right_node is not None:
                    num = self.right_node.balance(init_num=init_num)
                else:
                    self.right_node.root = init_num
                    self.left_node = self.left_node.left_node
        return self.root

    def print(self):
        self.balance()
        print(self.tree)

def build_tree(numbers: list) -> BST:

    for i, num in enumerate(numbers):
        if i == 0:
            tree = BST(number=num)
        tree.insert(num=num)

    return tree

if __name__ == "__main__":
    numbers = [4,2,9,10,1,0,8,13]

    bst = build_tree(numbers=numbers)