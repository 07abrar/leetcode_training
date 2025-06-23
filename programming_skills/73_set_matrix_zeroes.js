/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    const zeroesRow = new Set();
    const zeroesColumn = new Set();
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] === 0) {
                zeroesRow.add(i);
                zeroesColumn.add(j);
            };
        };
    };
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (zeroesRow.has(i) || zeroesColumn.has(j)) {
                matrix[i][j] = 0;
            };
        };
    };
    return matrix
};


let mat1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]];
console.log(setZeroes(mat1));

let mat2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]];
console.log(setZeroes(mat2));

let mat3 = [[-4, -2147483648, 6, -7, 0],
              [-8, 6, -8, -6, 0], [2147483647, 2, -9, -6, -10]];
console.log(setZeroes(mat3));