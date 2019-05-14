/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortedSquares = function(A) {
    // A = A.map(square);
    // A.sort(function(a,b){return a-b});
    return A.map(square).sort(function(a,b){return a-b});
};
function square(x){
    return x*x;
}
var a = [-4,-1,0,3,10];
console.log(sortedSquares(a));
