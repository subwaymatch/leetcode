class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        # Current_node represents a node in trie
        current_node = self.trie
        
        for c in word:
            if c not in current_node:
                current_node[c] = {}
            
            current_node = current_node[c]
        
        # Add an end of word mark
        current_node["end"] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        result = self.searchFromIndex(word, 0, self.trie)
        
        return result
    
    def searchFromIndex(self, word: str, idx: int, node: dict) -> bool:
        if idx == len(word):
            return "end" in node
        
        elif word[idx] == '.':
            for c in node:
                if self.searchFromIndex(word, idx + 1, node[c]):
                    return True
                
        elif word[idx] in node:
            return self.searchFromIndex(word, idx + 1, node[word[idx]])
                
        return False
