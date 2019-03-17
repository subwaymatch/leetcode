class Solution:
    def reverseVowels(self, s: str) -> str:
        # Since python doesn't support in-place string char replacement using indices (myString[1] = 'c' will throw an error)
        s_list = list(s)

        # Left/right pointers
        lp = 0
        rp = len(s_list) - 1
        vowels_map = {
            'a': True,
            'e': True, 
            'i': True, 
            'o': True,
            'u': True
        }

        while lp < rp:
            if s_list[lp].lower() not in vowels_map:
                lp += 1
                continue
                
            elif s_list[rp].lower() not in vowels_map:
                rp -= 1
                continue

            # Python swap characters in a string?
            temp = s_list[lp]
            s_list[lp] = s_list[rp]
            s_list[rp] = temp
            
            lp += 1
            rp -= 1

        return ''.join(s_list)
