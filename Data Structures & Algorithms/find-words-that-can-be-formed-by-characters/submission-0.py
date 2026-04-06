class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        charsCounter = Counter(chars)
        for word in words:
            wordCounter = Counter(word)
            good = True
            for c in wordCounter:
                if wordCounter[c] > charsCounter[c]:
                    good = False
                    break
            if good:
                res += len(word)
        
        return res      