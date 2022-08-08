class MyStack:

    def __init__(self):
        self.container = deque()
        

    def push(self, x: int) -> None:
        self.container.append(x)
        for _ in range(len(self.container)-1):
            self.container.append( self.container.popleft() )
    def pop(self) -> int:
        return self.container.popleft()
        

    def top(self) -> int:
        return self.container[0]

    def empty(self) -> bool:
        return(not self.container)
        # if(self.container == None):
        #     return(True)
        # return(False)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()