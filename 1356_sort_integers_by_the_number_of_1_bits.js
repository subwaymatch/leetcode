/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function(arr) {
    arr.sort(compareBits);
    return arr;
};

var compareBits = function(n1, n2) {
    bits1 = countBits(n1);
    bits2 = countBits(n2);
    
    if (bits1 === bits2) {
        return n1 > n2 ? 1 : -1;
    } else {
        return bits1 > bits2 ? 1 : -1;
    }
};

var countBits = function(num) {
    let numBits = 0;
    
    while (num > 0) {
        numBits += num & 1;
        num = num >> 1;
    }
    
    return numBits;
};
