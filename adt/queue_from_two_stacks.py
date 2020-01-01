class Queue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        return self.in_stack.append(item)

    def dequeue(self):
        if self.out_stack:
            return self.out_stack.pop()
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise Exception("Queue empty!")
        return self.out_stack.pop()

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def peek(self):
        if self.out_stack:
            return self.out_stack[-1]
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        if self.out_stack:
            return self.out_stack[-1]
        else:
            return None


def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.size())
    print(queue.peek())
    print(queue.dequeue())
    print(queue.peek())


if __name__ == '__main__':
    main()
