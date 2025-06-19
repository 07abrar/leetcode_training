/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let maxWealth = 0;
    for (let customer of accounts){
        let sum = customer.reduce((acc, num) => acc + num, 0);
        maxWealth = Math.max(maxWealth, sum)
    }
    return maxWealth;
};


let accounts1 = [[1, 2, 3], [3, 2, 1]];
console.log("Example 1 Output:", maximumWealth(accounts1));


let accounts2 = [[1, 5], [7, 3], [3, 5]];
console.log("Example 2 Output:", maximumWealth(accounts2));