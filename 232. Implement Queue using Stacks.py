#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 初始化栈
        self.stack_in = []
        self.stack_out = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack_out:
            return self.stack_out[-1]
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack_in and not self.stack_out

if __name__ == '__main__':


    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()