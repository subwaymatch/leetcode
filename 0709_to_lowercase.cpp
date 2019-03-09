class Solution {
public:
    string toLowerCase(string str) {
        int asciiA = (int) 'A';
        int asciiZ = (int) 'Z'; 
        int diff = (int) 'a' - asciiA;
        
        for (char& c: str) {
            int charAscii = (int) c;
            
            if (c >= asciiA && c <= asciiZ) {
                c = (char)(c + diff);
            }
        }
        
        return str; 
    }
};
