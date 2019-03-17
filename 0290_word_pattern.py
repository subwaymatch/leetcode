        str = str.split(' ')
        pattern_to_word_map = {}
        word_to_pattern_map = {}

        if len(pattern) != len(str):
            return False

        for idx, c in enumerate(pattern):
            word = str[idx]
            if c not in pattern_to_word_map and word not in word_to_pattern_map:
                pattern_to_word_map[c] = word
                word_to_pattern_map[word] = c
            elif c in pattern_to_word_map and word in word_to_pattern_map:
                if pattern_to_word_map[c] != word or word_to_pattern_map[word] != c:
                    return False
            else:
                return False
        
        return True
