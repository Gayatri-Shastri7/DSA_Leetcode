class WordFilter:

    def __init__(self, words: List[str]):
        self.suffix=defaultdict(set)
        self.prefix=defaultdict(set)
        self.index={}
        for j in range(len(words)):
            for i in range(len(words[j])):
                self.suffix[words[j][i:]].add(words[j])
                self.prefix[words[j][:i+1]].add(words[j])
            self.index[words[j]]=j

    def f(self, prefix: str, suffix: str) -> int:
    

        
        maximum=-1
        for word in self.prefix[prefix].intersection(self.suffix[suffix]):
            
            maximum=max(maximum,self.index[word])
        
        return maximum