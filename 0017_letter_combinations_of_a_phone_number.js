var digitMap = {
    '2': ['a', 'b', 'c'], 
    '3': ['d', 'e', 'f'], 
    '4': ['g', 'h', 'i'], 
    '5': ['j', 'k', 'l'], 
    '6': ['m', 'n', 'o'], 
    '7': ['p', 'q', 'r', 's'], 
    '8': ['t', 'u', 'v'], 
    '9': ['w', 'x', 'y', 'z']
};

var findCombinations = function(digits, index, combinations) {
    if (index == digits.length) return combinations; 
    
    var digitChars = digitMap[digits[index]]; 
    var newCombinations = []; 
    
    for (var i = 0; i < digitChars.length; i++) {
        for (var j = 0; j < combinations.length; j++) {
            newCombinations.push(combinations[j] + digitChars[i]); 
        }
    }
    
    return findCombinations(digits, index + 1, newCombinations); 
};

/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (digits == "") return []; 
    
    return findCombinations(digits, 1, digitMap[digits[0]]); 
};
