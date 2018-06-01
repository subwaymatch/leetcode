class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int> countMap;
        char * currentCharAddr = (char *) s.c_str();

        int longestSubstringLength = 0;
        int currentSubstringLength = 0;
        int charIndex = 0;
        int startIndex = 0;
        bool isLastChar = false;
        bool isDebugMode = false;

        while (*currentCharAddr != '\0')
        {
            char currentChar = *currentCharAddr;

            if (*(currentCharAddr + 1) == '\0') isLastChar = true;

            if (isDebugMode) cout << "[" << currentChar << "]: cIndex=" << charIndex << ", startIndex=" << startIndex << ", currSubstrLen=" << currentSubstringLength << endl;

            if (countMap.count(currentChar) > 0)
            {
                if (isDebugMode) cout << "map[" << currentChar << "]=" << countMap[currentChar] << endl;

                if ((startIndex > countMap[currentChar]) && isLastChar)
                {
                    currentSubstringLength++;
                    if (isDebugMode) cout << "currentSubstringLength++ to " << currentSubstringLength << endl;
                }

                if (currentSubstringLength > longestSubstringLength) {
                    longestSubstringLength = currentSubstringLength;
                    if (isLastChar) break;
                }

                if (startIndex > countMap[currentChar])
                {
                    // currentSubstringLength = charIndex - startIndex;
                    currentSubstringLength = charIndex - startIndex + 1;
                }

                else
                {
                    currentSubstringLength = charIndex - countMap[currentChar];
                }

                if (countMap[currentChar] >= startIndex)
                {
                    startIndex = countMap[currentChar] + 1;
                }

                else
                {
                    // startIndex = charIndex;
                }

            }

            else
            {
                currentSubstringLength++;
            }

            countMap[currentChar] = charIndex;
            charIndex++;
            currentCharAddr++;

            if (isDebugMode) cout << "end startIndex=" << startIndex << ", map[" << currentChar << "]=" << countMap[currentChar] << ", currSubstrLen=" << currentSubstringLength << ", longestSubstrLen=" << longestSubstringLength << endl;
            if (isDebugMode) cout << endl;
        }

        if (currentSubstringLength > longestSubstringLength) {
            longestSubstringLength = currentSubstringLength;
            if (isDebugMode) cout << "666 currentSubstringLength=" << currentSubstringLength << ", longestSubstringLength=" << longestSubstringLength << " p2" << endl;
        }

        return  longestSubstringLength;
    }
};
