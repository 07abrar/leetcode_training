/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function(low, high) {
    let odd = 0;
    for(let i = low; i <= high; i++){
        if(i % 2 !== 0){
            odd += 1;
        };
    };
    return odd;
};


let low1 = 3, high1 = 7;
console.log(countOdds(low1, high1));

let low2 = 8, high2 = 10;
console.log(countOdds(low2, high2));