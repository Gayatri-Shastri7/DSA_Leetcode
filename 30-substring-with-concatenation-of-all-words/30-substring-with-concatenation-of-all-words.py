class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_w, n_words, cnt_words = len(words[0]), len(words), Counter(words)
        return [i for i in range(len(s) + 1 - len_w * n_words)
                if s[i: i + len_w] in cnt_words and
                Counter(s[i + j * len_w: i + (j + 1) * len_w]
                        for j in range(n_words)) == cnt_words]
