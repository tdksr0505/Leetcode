class Solution {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        int i;
        for(i = 0;i+1<nums.length;i+=2){
            if(nums[i]!=nums[i+1])
                return nums[i];
        }
        return nums[i];
    }
}