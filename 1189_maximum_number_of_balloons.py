class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_counter = collections.Counter(text)
        word_counter = collections.Counter('balloon')
        
        return min([text_counter[c] // word_counter[c] for c in word_counter])
