/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    const indices = [];
    
    nums.sort((a, b) => a - b);
    
    nums.forEach((n, i) => {
        if (n == target) {
            indices.push(i)
        }
    });

    return indices;
};
