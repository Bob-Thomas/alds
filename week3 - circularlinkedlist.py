class ListNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)


class MyCircularLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.tail
        if current != None:
            s = s + str(current)
            current = current.next
        while current != None and current != self.tail:
            s = s + " -> " + str(current)
            current = current.next
        if not s:  # s == '':
            s = 'empty list'
        return s

    def append(self, e):
        if not self.tail:
            self.tail = ListNode(e, self)
            self.tail.next = self.tail
        else:
            self.tail.next = ListNode(e, self.tail.next)
            self.tail = self.tail.next

    def delete(self, e):
        if self.tail:  # self.head != None:
            if self.tail.data == e:
                if self.tail.next == self.tail:
                    self.tail = None
                else:
                    self.tail = self.tail.next
            else:
                current = self.tail
                while current.next != None and current.next.data != e:
                    current = current.next
                if current.next != None:
                    current.next = current.next.next
                if current.next == None:
                    self.tail = current


if __name__ == '__main__':
    mylist = MyCircularLinkedList()
    print(mylist)
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    mylist.append(4)
    mylist.append(5)
    mylist.append(6)
    print(mylist)
    mylist.append(7)
    mylist.append(8)
    mylist.append(9)
    mylist.append(10)
    mylist.append(11)
    mylist.append(12)
    print(mylist)
    mylist.delete(1)
    mylist.delete(2)
    mylist.delete(3)
    mylist.delete(4)
    mylist.delete(5)
    print(mylist)
    mylist.append(10)
    print(mylist)
