class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] = count[word] + 1
        
        word_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        
        result = list(map(lambda x: x[0], word_items[:k]))
        
        return result
