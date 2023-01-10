/**
 * @param {number[]} nums
 * @return {number}
 */
var averageValue = function(nums) {
    const filteredNums = nums.filter(n => (n % 3 == 0) & (n % 2 == 0));
    return filteredNums.length > 0 ? Math.floor(filteredNums.reduce((a, b) => a + b, 0) / filteredNums.length) : 0;
};
