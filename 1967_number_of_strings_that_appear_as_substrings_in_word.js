/**
 * @param {string[]} patterns
 * @param {string} word
 * @return {number}
 */
var numOfStrings = function(patterns, word) {
    return patterns.reduce(
        (prev, curr) => prev + (word.includes(curr) | 0),
        0
    );
};
