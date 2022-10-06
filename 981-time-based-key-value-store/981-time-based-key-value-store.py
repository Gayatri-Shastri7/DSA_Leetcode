class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].update({timestamp:value})
        else:
            self.dict.update({key:{timestamp:value}})

    def get(self, key: str, timestamp: int) -> str:
        for x in range(timestamp):
            try:
                return self.dict[key][timestamp-x]
            except:
                pass
        return ""

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)