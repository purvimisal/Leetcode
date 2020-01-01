class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def getData(self):
        return self.value

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.value = newdata

    def setNext(self, newnext):
        self.next = newnext


class LinkList(object):
    def __init__(self):
        self.head = None
        self.lenght = 0

    def addNode(self, value):
        temp = self.head
        node = Node(value)
        node.next = temp
        self.head = node
        self.lenght += 1

    def printList(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def deleteNode(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.next
            i += 1
        if index == i:
            self.lenght -= 1
            if prev == None:
                self.head = node.next
            else:
                prev.next = node.next
        else:
            print('Index not found')


def main():
    ll = LinkList()
    print(ll.lenght)
    ll.addNode(1)
    ll.addNode(2)
    ll.addNode(3)
    print(ll.lenght)
    ll.printList()
    ll.deleteNode(4)
    ll.printList()
    print(ll.lenght)


if __name__ == '__main__':
    main()
