'''

Attack & Defense

'''

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (-x[0], x[1]))
        maxDef = 0
        count = 0
        for arr in properties:
            if arr[1] < maxDef:
                count += 1
            else :
                maxDef = arr[1]
        return count