class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


class StackwithNodes(object):
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return bool(self.top)

    def pop(self):
        node = self.top
        if node:
            self.top = node.next
            return node.value
        else:
            raise Exception('Stack is empty.')

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def size(self):
        node = self.top
        if node != None:
            num_nodes = 1
        else:
            return 0
        node = node.next
        while node:
            num_nodes += 1
            node = node.next
        return num_nodes

    def peek(self):
        return self.top.value


def main():
    stack = StackwithNodes()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())


if __name__ == '__main__':
    main()
