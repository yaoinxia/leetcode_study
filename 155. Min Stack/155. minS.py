class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.front = None

    def push(self, x: int) -> None:
        if not self.s:
            self.front = x
        self.s.append(x)

    def pop(self) -> None:
        self.s.pop()
        # if self.s:
        #     self.s.remove(self.s[-1])

    def top(self) -> int:
        if not self.s:
            return self.front
        else:
            return self.s[-1]

    def getMin(self) -> int:
        # print(sorted(self.s))
        # print(self.s.sort())
        return sorted(self.s)[0]

if __name__ == '__main__':
    m = MinStack()
    m.push(-2);
    m.push(0);
    m.push(-3);
    print(m.s)
    m.pop()
    print(m.s)
    m.pop()
    print(m.s)
    m.pop()
    print(m.s)

    # print(m.top())
    # print(m.getMin())
