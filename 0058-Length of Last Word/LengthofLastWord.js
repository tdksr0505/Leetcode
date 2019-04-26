/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    s = s.trim();
    var n = -1;
    for(var i  = 0;i<s.length-1;i++){
        if(s[i]==" " && s[i+1]!=" "){
            n = i;
        }
    }
    return s.length - (n+1);
    // return s.trim().split(" ").reverse()[0].length
};


console.log(lengthOfLastWord("adsd as"));
