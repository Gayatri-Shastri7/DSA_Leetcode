class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        unmatched_indexes = set()
        unmatched_values = set()
        chunks = 0
        for index, value in enumerate(arr):
            if index != value:
                if index in unmatched_values:
                    unmatched_values.remove(index)
                else:
                    unmatched_indexes.add(index)
                if value in unmatched_indexes:
                    unmatched_indexes.remove(value)
                else:
                    unmatched_values.add(value)
            if not any([unmatched_indexes, unmatched_values]):
                chunks += 1
        return chunks