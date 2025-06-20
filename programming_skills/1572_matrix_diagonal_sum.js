/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    let diagonal = 0;
    for (const [i,row] of mat.entries()){
        for (const [j,num] of row.entries()){
            if (i == j){
                diagonal += num;
            }
            else if (mat.length-1-i == j){
                diagonal += num;
            };
        };
    };
    return diagonal;
};

let mat1 = [[1,2,3],
              [4,5,6],
              [7,8,9]];
console.log(diagonalSum(mat1));


let mat2 = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]];
console.log(diagonalSum(mat2));