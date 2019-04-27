/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    var count = 0;
    for(var i = 0 ; i<nums.length;){
        if(nums[i] == val){
            nums.splice(i, 1);
        }
        else{
            i++;
        }
    }
    return nums.length;
};

var nums = [3,2,2,3];
console.log(removeElement(nums, 3));
