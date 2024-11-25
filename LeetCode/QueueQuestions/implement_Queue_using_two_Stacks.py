class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
       self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                val = self.stack1.pop()
                self.stack2.append(val)
        return self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                val = self.stack1.pop()
                self.stack2.append(val)
        return self.stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
       return max(len(self.stack1), len(self.stack2)) == 0
        # if len(self.stack1)== 0 and len(self.stack2) == 0:
        #     return True
        # else:
        #     return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()