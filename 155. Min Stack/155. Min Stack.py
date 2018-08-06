class MinStack:
  # @param x, an integer
  # @return an integer
  def __init__(self):
    self.stack = []
    self.minStack = [] #最小值栈 （最小值，出现次数）

  def push(self, x):
    self.stack.append(x)
    #如果 新增值x == 最小值栈顶的值
    if len(self.minStack) and x == self.minStack[-1][0]:
      #最小值栈顶元素次数+1
      print("=========================")
      print(self.minStack[-1][0])
      print("+++++++++++++++++++++++++")
      self.minStack[-1] = (x, self.minStack[-1][1] + 1)
    #如果 最小值栈为空，或者新增值 < 最小值栈顶的值
    elif len(self.minStack) == 0 or x < self.minStack[-1][0]:
      #x入最小值栈
      self.minStack.append((x, 1))

  def pop(self):
    #如果 栈顶值 == 最小值栈顶值
    if self.top() == self.getMin():
      #如果 最小值栈顶元素次数 > 1
      if self.minStack[-1][1] > 1:
        #最小值栈顶元素次数 - 1
        self.minStack[-1] = (self.minStack[-1][0], self.minStack[-1][1] - 1)
      else:
        #最小值栈顶元素弹出
        self.minStack.pop()
    return self.stack.pop()

  def top(self):
    return self.stack[-1]

  def getMin(self):
    return self.minStack[-1][0]

if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    print(str(obj))
    obj.push(1)
    obj.push(2)
    obj.push(-8)
    obj.push(-2)
    obj.push(-9)
    print(str(obj))
    #obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print("栈顶部的元素为：" + str(param_3))
    print("栈中最小值为：" + str(param_4))
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
