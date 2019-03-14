class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        min_length = sys.maxsize
        max_length = 0
        word_dict = {}
        
        for word in wordDict:
            word_dict[word] = True
        
            min_length = min(min_length, len(word))
            max_length = max(max_length, len(word))
    
        if min_length > len(s):
            return False
            
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        dp[-min_length - 1] = s[-min_length:] in word_dict
        
        for start_idx in reversed(range(len(s) - min_length)):
            for str_len in range(1, min(max_length + 1, len(s) - start_idx + 1)):
                word = s[start_idx:start_idx + str_len]
                
                if word in word_dict and dp[start_idx + str_len]:
                    dp[start_idx] = True
                    break
            
        return dp[0]
