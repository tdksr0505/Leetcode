/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    var array = [];
    array[0] = 1;
    array[1] = 1;
    array[2] = 2;

    for(var i = 2;i<=n;i++){
        array[i] = array[i-1] + array[i-2];
    }
    return array[n];
};

console.log(climbStairs(45));
