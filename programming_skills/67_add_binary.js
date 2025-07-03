/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let arrA = a.split('');
    let arrB = b.split('');
    let res = [];
    let carry = 0;

    while (arrA.length || arrB.length || carry) {
        if (arrA.length > 0) {
            carry += Number(arrA.pop());
        }
        if (arrB.length > 0) {
            carry += Number(arrB.pop());
        }
        res.push(carry % 2);
        carry = Math.floor(carry / 2);
    }

    return res.reverse().join('')
};


let a1 = "11", b1 = "1"
console.log(addBinary(a1, b1));

let a2 = "1010", b2 = "1011"
console.log(addBinary(a2, b2));