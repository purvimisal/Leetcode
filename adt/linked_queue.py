class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue(object):
    def __init__(self):
        self.front = None
        self.back = None

    def isEmpty(self):
        return bool(self.front) and bool(self.back)

    def dequeue(self):
        if self.front:
            value = self.front.value
            self.front = self.front.next
            return value
        raise Exception('Queue is empty, cannot dequeue.')

    def enqueue(self, value):
        node = Node(value)
        if self.front:
            self.back.next = node
        else:
            self.front = node
        self.back = node
        return True

    def size(self):
        node = self.front
        if node:
            num_nodes = 1
            node = node.next
            while node:
                num_nodes += 1
                node = node.next
        return num_nodes

    def peek(self):
        return self.front.value


def main():
    queue = LinkedQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.size())
    print(queue.peek())
    print(queue.dequeue())
    print(queue.peek())


if __name__ == '__main__':
    main()
