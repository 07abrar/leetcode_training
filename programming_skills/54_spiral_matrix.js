/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    let row = 0, col = 0, drow = 0, dcol = 1;
    const spiralMat = []

    for (let i = 0; i < matrix.length * matrix[0].length; i++) {
        spiralMat.push(matrix[row][col]);
        matrix[row][col] = null;
        if (row + drow >= matrix.length ||
            col + dcol >= matrix[0].length ||
            row + drow < 0 ||
            col + dcol < 0 ||
            matrix[row + drow][col + dcol] === null
        ) {
            [drow, dcol] = [dcol, -drow];
        }
        row += drow;
        col += dcol;
    }
    return spiralMat;
};


let mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
console.log(spiralOrder(mat1));

let mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]];
console.log(spiralOrder(mat2));

let mat3 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]];
console.log(spiralOrder(mat3));