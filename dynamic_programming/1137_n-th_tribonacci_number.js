/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) {
    if (n==0) {
        return 0;
    }
    else if (n==1) {
        return 1;
    }
    else if (n==2) {
        return 1;
    }
    else{
        let dinamic_list = new Array(n+1).fill(0);
        dinamic_list[0] = 0;
        dinamic_list[1] = 1;
        dinamic_list[2] = 1;
        for (let i = 3; i < n+1; i++) {
            dinamic_list[i] = (dinamic_list[i-1] +
                dinamic_list[i-2] +
                dinamic_list[i-3]
            );
        }
        return dinamic_list[dinamic_list.length - 1];
    };
};

var n = 2;
console.log(tribonacci(n));

var n = 4;
console.log(tribonacci(n));

var n = 25;
console.log(tribonacci(n));