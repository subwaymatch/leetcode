/**
 * @param {number[][]} A
 * @return {number[][]}
 */
var flipAndInvertImage = function(A) {
    return A.map(function(row) {
        for (var i = 0; i < Math.floor(row.length / 2); i++) {
            var temp = row[i]; 
            row[i] = row[row.length - 1 - i]; 
            row[row.length - 1 - i] = temp;
        }
        
        return row.map(function(n) { return (n == 0) ? 1 : 0; }); 
    });
};
