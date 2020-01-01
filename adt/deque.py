class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __repr__(self):
        return '{}'.format(self.items)


def main():
    dq = Deque()
    dq.addFront(1)
    dq.addFront(2)
    dq.addFront(3)
    dq.addRear(40)
    dq.addRear(50)
    print(dq.size())
    print(dq)


if __name__ == '__main__':
    main()
