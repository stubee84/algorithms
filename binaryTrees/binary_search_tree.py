class BST:
    def __init__(self, number: int):
        self.tree: list = []
        self.left_node = None
        self.right_node = None
        self.root: int = number
        self.depth: int = 0
        self.left_count: int = 0
        self.right_count: int = 0
        self.total_count: int = 1

    def insert(self, num: int) -> tuple:
        if num < self.root:
            #in a balanced tree the left depth will always be greater than or equal to the right
            if self.left_node is not None:
                depthAndCount = self.left_node.insert(num=num)
                self.depth += depthAndCount[0]
                self.left_count += depthAndCount[1]
                self.total_count += self.left_count
                self.balance_left()
            else:
                self.left_node = BST(number=num)
                self.depth += 1
                self.left_count += 1
                self.total_count += 1
        elif num > self.root:
            if self.right_node is not None:
                depthAndCount = self.right_node.insert(num=num)
                self.right_count += depthAndCount[1]
                self.total_count += self.right_count
            else:
                self.right_node = BST(number=num)
                self.total_count += 1
                self.right_count += 1

        return self.depth, self.total_count

    def remove(self, num: int):
        if num < self.root:
            if self.left_node is not None:
                self.left_node.remove(num=num)
        elif num > self.root:
            if self.right_node is not None:
                self.right_node.remove(num=num)
        else:
            if self.left_count > self.right_count:
                next_root = self.left_node.get_greatest_left()
            elif self.left_count == self.right_count:
                next_root = self.right_node.get_least_right()
            self.root = next_root
        return

    def get_greatest_left(self) -> int:
        if self.right_node is not None:
            value = self.right_node.get_greatest_left()
            #balance the sub_tree
            self.balance_left()
        else:
            self.total_count -= 1
            self.left_count -= 1

            if self.left_node is not None:
                value = self.root
                self.root = self.left_node.root
                self.left_node = None
                self.depth -= 1
            else:
                value = self.root
                self = None
        return value

    def get_least_right(self) -> int:
        if self.left_node is not None:
            value = self.left_node.get_least_right()
            self.balance_right()
        else:
            self.total_count -= 1
            self.right_count -= 1

            value = self.root
            self = None
        return value

    #dfs style search
    def search(self, num: int):
        if self.root == num:
            return self
        elif self.root < num:
            self.right_node.search(num=num)
        elif self.root > num:
            self.left_node.search(num=num)
        else:
            return None

    def balance_left(self):
        if self.left_node.left_node is not None:
            new_root = self.left_node.root
            self.right_node = BST(number=self.root)
            self.root = new_root
            self.left_node.root = self.left_node.left_node.root
            self.left_node.left_node = None
    
    def balance_right(self):
        if self.right_node.left_node is not None:
            new_root = self.right_node.left_node.root
            self.left_node = BST(number=self.root)
            self.root = new_root
            self.right_node.left_node = None
        else:
            new_root = self.right_node.root
            self.left_node = BST(number=self.root)
            self.root = new_root
            self.right_node = None

    def build_sorted_list(self):
        if self.left_node is not None:
            self.tree += self.left_node.build_sorted_list()
        self.tree.append(self.root)
        if self.right_node is not None:
            self.tree += self.right_node.build_sorted_list()
        return self.tree

def build_tree(numbers: list) -> BST:

    for i, num in enumerate(numbers):
        if i == 0:
            tree = BST(number=num)
        tree.insert(num=num)

    return tree

if __name__ == "__main__":
    numbers = [4,2,9,10,1,0,8,13]

    bst = build_tree(numbers=numbers)
    bst.build_sorted_list()
    print(bst.tree)