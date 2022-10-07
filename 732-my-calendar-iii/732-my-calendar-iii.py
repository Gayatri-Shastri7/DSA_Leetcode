from sortedcontainers import SortedList
class MyCalendarThree:

    def __init__(self):
        self.st = SortedList()
        self.m = 0

    def book(self, start: int, end: int) -> bool:
        self.st.add([start,1])
        self.st.add([end,-1])
        c = 0
        for i,j in self.st:
            c += j 
            self.m = max(self.m,c)
        return self.m

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)