from queue import Queue


class BSTNode:
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

    def __repr__(self, nspaces=0):
        s1 = ''
        s2 = ''
        s3 = ''
        if self.right != None:
            s1 = self.right.__repr__(nspaces + 3)
        s2 = s2 + ' ' * nspaces + str(self.element) + '\n'
        if self.left != None:
            s3 = self.left.__repr__(nspaces + 3)
        return s1 + s2 + s3

    def max(self):
        found = False
        if self.right and self.element < self.right.element:
            found = self.right.max()
        elif self.left and self.element < self.left.element:
            found = self.left.max()
        return found if found else self

    def insert(self, e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left
        else:
            found = True

        while not found and current:
            parent = current
            if parent.element < e:
                current = parent.right
            elif parent.element > e:
                current = parent.left
            else:
                found = True

        if not found:
            if parent.element < e:
                parent.right = BSTNode(e, None, None)
            else:
                parent.left = BSTNode(e, None, None)
        return not found

    def rinsert(self, e):
        if self.element == None:
            self = BSTNode(e, None, None)
            return True
        elif self.element < e:
            if self.right != None:
                return self.right.rinsert(e)
            else:
                self.right = BSTNode(e, None, None)
                return True
        elif self.element > e:
            if self.left != None:
                return self.left.rinsert(e)
            else:
                self.left = BSTNode(e, None, None)
                return True
        elif self.element == e:
            return False

    def insertArray(self, a, low=0, high=-1):
        if len(a) == 0:
            return
        if high == -1:
            high = len(a) - 1
        mid = (low + high + 1) // 2
        self.insert(a[mid])
        if mid > low:
            self.insertArray(a, low, mid - 1)
        if high > mid:
            self.insertArray(a, mid + 1, high)

    def search(self, e):
        current = self
        found = False
        while not found and current:
            if current.element < e:
                current = current.right
            elif current.element > e:
                current = current.left
            else:
                found = True
        if found:
            return current
        else:
            return None

    def rsearch(self, e):
        found = False
        if self.element == e:
            return self
        if self.left and e < self.element:
            found = self.left.rsearch(e)
        elif self.right:
            found = self.right.rsearch(e)

        return None if not found else found

    def search2(self, e):
        if self.element == e:
            return self

        parent = self.getParent(e)
        if parent == None:
            return None
        if parent.element < e:
            return parent.right
        return parent.left

    def getParent(self, e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left
        else:
            return None

        while not found and current:
            if current.element == e:
                found = True
            else:
                parent = current
                if current.element < e:
                    current = current.right
                else:
                    current = current.left
        if found:
            return parent
        else:
            return None

    def parentMinRightTree(self):
        parent = self.right
        current = parent.left
        while current.left:
            parent = current
            current = current.left
        return parent

    def delete(self, e):
        parent = self.getParent(e)

        if parent == None:
            return False
        if parent.element < e:
            current = parent.right
            if current.left == None:
                parent.right = parent.right.right
                return True
            else:
                if current.right == None:
                    parent.right = parent.right.left
                    return True
        else:
            current = parent.left
            if current.left == None:
                parent.left = parent.left.right
                return True
            else:
                if current.right == None:
                    parent.left = parent.left.left
                    return True
        if current.right.left == None:
            current.element = current.right.element
            current.right = current.right.right
            return True
        node = current.parentMinRightTree()
        current.element = node.left.element
        node.left = node.left.right
        return True


class BST:
    def __init__(self, a=None):
        if a:
            mid = len(a) // 2
            self.root = BSTNode(a[mid], None, None)
            self.root.insertArray(a[:mid])
            self.root.insertArray(a[mid + 1:])
        else:
            self.root = None

    def __repr__(self):
        if self.root:
            return str(self.root)
        else:
            return 'null-tree'

    def showLevelOrder(self):
        if not self.root:
            return 'null-tree'

        level = 0
        currentLevel = [self.root]
        while currentLevel:
            level+=1
            print('LEVEL - ', level)
            next = list()
            for n in currentLevel:
                print(n.element)
                if n.left: next.append(n.left)
                if n.right: next.append(n.right)
            print
            currentLevel = next

    def search(self, e):
        if self.root and e:
            return self.root.search(e)
        else:
            return None

    def insert(self, e):
        if e:
            if self.root:
                return self.root.insert(e)
            else:
                self.root = BSTNode(e, None, None)
                return True
        else:
            return False

    def rinsert(self, e):
        if e:
            if self.root:
                return self.root.rinsert(e)
            else:
                self.root = BSTNode(e, None, None)
                return True
        else:
            return False

    def delete(self, e):
        if self.root and e:
            if self.root.element == e:
                if self.root.left == None:
                    self.root = self.root.right
                elif self.root.right == None:
                    self.root = self.root.left
                elif self.root.right.left == None:
                    self.root.element = self.root.right.element
                    self.root.right = self.root.right.right
                else:
                    node = self.root.parentMinRightTree()
                    self.root.element = node.left.element
                    node.left = node.left.right
                return True
            else:
                return self.root.delete(e)
        else:
            return False

    def max(self):
        return self.root.max()

    def rsearch(self, e):
        return self.root.rsearch(e)


if __name__ == '__main__':
    b = BST([1, 2, 3])
    print(b)
    b.showLevelOrder()

    print('----------------')
    b = BST([1, 2, 3, 4])
    print(b)
    b.showLevelOrder()

    print('----------------')
    b = BST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(b)
    b.showLevelOrder()

    print('----------------')

    b = BST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print(b)
    b.showLevelOrder()

    node = b.rsearch(3)
    assert(node != None)
    node = b.rsearch(4)
    assert(node != None)
    node = b.rsearch(8)
    assert(node != None)
    node = b.rsearch(11)
    assert(node != None)
    node = b.rsearch(16)
    assert(node == None)

    b.insert(17)
    print(b)

    print('----------------')
    b.delete(14)
    print(b)
    print('----------------')

    print(b.insert(10))

    b = BST()
    for i in range(1, 11):
        b.insert(i)
    print(b)

    print('----------------')

    b = BST(None)
    print(b)
    print('----------------')
    b = BST([])
    print(b)
    print('----------------')
    b = BST([0])
    print(b)
    print('----------------')

    b = BST()
    b.rinsert(3)
    b.rinsert(2)
    b.rinsert(10)
    b.rinsert(11)
    b.rinsert(9)
    b.rinsert(6)
    b.rinsert(7)
    b.rinsert(8)
    print("Recursief toevoegen is hier: ")
    print(b)

    print('----------------')
    b.delete(3)
    print(b)

    print('----------------')