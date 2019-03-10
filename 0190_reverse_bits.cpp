class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result = 0;

        for (int i = 0; i < 16; i++) {
            uint32_t left = (n & (1 << 31 - i)) >> (31 - i);
            uint32_t right = (n & (1 << i)) >> i; 

            result = result | (left << i) | (right << (31 - i));
        }

        return result;  
    }
};
