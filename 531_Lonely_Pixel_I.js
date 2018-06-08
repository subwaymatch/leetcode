/**
 * @param {character[][]} picture
 * @return {number}
 */
var findLonelyPixel = function(picture) {
    var isBlackInRow = []; 
    var isBlackInCol = []; 
    
    var numRows = picture.length; 
    var numLonelyPixels = 0; 
    
    if (numRows == 0) return 0; 
    
    var numCols = picture.length > 0 ? picture[0].length : 0; 
    
    // Check rows/columns for black and white cells
    for (var row = 0; row < numRows; row++) {
        isBlackInRow[row] = 0; 
        
        for (var col = 0; col < picture[0].length; col++) {
            if (picture[row][col] == 'B') {
                isBlackInRow[row]++; 
                if (isBlackInRow >= 2) break; 
            }
        }
    }
    
    for (var col = 0; col < numCols; col++) {
        isBlackInCol[col] = 0; 
        
        for (var row = 0; row < numRows; row++) {
            if (picture[row][col] == 'B') {
                isBlackInCol[col]++; 
                
                if (isBlackInCol >= 2) break; 
            }
        }
    }
    
    for (var row = 0; row < numRows; row++) {
        for (var col = 0; col < numCols; col++) {
            if (picture[row][col] == 'B' && isBlackInRow[row] == 1 && isBlackInCol[col] == 1) numLonelyPixels++; 
        }
    }
    
    
    return numLonelyPixels; 
};
